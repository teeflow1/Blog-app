
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category, Comment
from . forms import PostForm, EditForm, EditCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

#def home(request):
 #   return render(request, "apps/home.html", {})
 
 
def LikeView(request, pk):
    post = get_object_or_404 (Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


    
    
     
class HomeView(ListView):
    model = Post
    template_name = 'apps/home.html'
    ordering = ['-posted_at']
    
    
    
class DetailProjectView(DetailView):
    model = Post
    template_name = 'apps/details.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(DetailProjectView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context ["total_likes"] = total_likes
        return context
    
    
       
class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'apps/add_blog.html'
    #fields = '__all__'
    
class AddCommentView(CreateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'apps/add_comment.html'
    #fields = '__all__'
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    
    
    
class AddCategoryView(CreateView):
    model = Category
    #form_class = EditForm
    template_name = 'apps/add_category.html'
    fields = '__all__'
    
class EditPostView(UpdateView):
    model = Post
    template_name = 'apps/edit_post.html'
    form_class = EditForm
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'apps/delete_post.html'
    success_url = reverse_lazy('home')
    

    
 
