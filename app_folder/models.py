from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
    
class Category (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('home')
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    upload_image = models.ImageField(null=True, blank=True, upload_to ='images/')
    title_tag = models.CharField(max_length=250, default='This is a blog Web App!')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    posted_at = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Technology')
    snippet = models.CharField(max_length=255, default="Click to View Post")
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
    def get_absolute_url(self):
        return reverse('home')
    
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=250, null=True, blank=True)
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)
    linkedin_url = models.CharField(max_length=250, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.user)
    
    
    def get_absolute_url(self):
        return reverse('home')
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse('home')