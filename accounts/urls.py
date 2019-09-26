from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('accounts/', views.index),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('addslide/', views.addslide),
    path('articals/', views.articals),
    path('edit/<int:myid>', views.edit),
    path('post/<int:myid>', views.post),
    path('delete/<int:myid>', views.delete),



   


    

]