from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('admin/', views.admin),
    path('post/<int:myid>', views.post),
    path('posts/<int:myid>', views.posts),
    #path('addslide/', views.addslide),
    #path('articals/', views.articals),


    

]
