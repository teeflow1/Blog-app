from django import forms
from .models import Post,Category,Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category','body', 'snippet','upload_image')
        
        widgets = {
            'title':  forms.TextInput (attrs = {'class': 'form-control'}),
            'title_tag':  forms.TextInput (attrs = {'class': 'form-contorl'}),
            'author':  forms.TextInput (attrs = {'class': 'form-contorl', 'value': '', 'id':'admin', 'type': 'hidden'}),
            #'author':  forms.Select (attrs = {'class': 'form-contorl'}),
            'category':  forms.Select ( choices = choice_list, attrs = {'class': 'form-contorl'}),
            'body':  forms.Textarea (attrs = {'class': 'form-contorl'}),
            'snippet':  forms.Textarea (attrs = {'class': 'form-contorl'})
        }
        
        

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag',  'body', 'snippet')
        
        widgets = {
            'title':  forms.TextInput (attrs = {'class': 'form-control',}),
            'title_tag':  forms.TextInput (attrs = {'class': 'form-contorl'}),
            #'author':  forms.Select (attrs = {'class': 'form-contorl'}),
            'body':  forms.Textarea (attrs = {'class': 'form-contorl'}),
            'snippet':  forms.Textarea (attrs = {'class': 'form-contorl'})
        }
        
        
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets = {
            'name':  forms.TextInput (attrs = {'class': 'form-control',}),
            #'title_tag':  forms.TextInput (attrs = {'class': 'form-contorl'}),
            #'author':  forms.Select (attrs = {'class': 'form-contorl'}),
            'body':  forms.Textarea (attrs = {'class': 'form-contorl'})
        }
        
        

