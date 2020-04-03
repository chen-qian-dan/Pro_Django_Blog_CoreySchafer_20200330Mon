from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView
)
from . import views # . means current repository 

# better always put '/' after the address
urlpatterns = [
    #'' means home page, 
    # it means if people add nothing after the website address,
    # then return the home page. And the home page is on views.home
    path('', PostListView.as_view(), name='blog-home'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('about/', views.about, name='blog-about'),
]