from django.urls import path
from . import views # . means current repository 

# better always put '/' after the address
urlpatterns = [
    #'' means home page, 
    # it means if people add nothing after the website address,
    # then return the home page. And the home page is on views.home
    path('', views.home, name='blog-home'),  
    path('about/', views.about, name='blog-about'),
]