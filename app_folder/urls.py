from django.urls import path
from .views import HomeView, DetailProjectView, AddBlogView, EditPostView,DeletePostView, AddCategoryView, AddCommentView, LikeView

urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', DetailProjectView.as_view(), name = 'details'),
    path('add_blog/', AddBlogView.as_view(), name = 'add_blog'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('aritcle/edit/<int:pk>',EditPostView.as_view(), name = "edit_post" ),
    path('aritcle/<int:pk>/remove',DeletePostView.as_view(), name = "delete_post" ),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_post_comment'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
]
