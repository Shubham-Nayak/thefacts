from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('admin/', views.admin),
    path('post/<str:myurl>', views.post),
    path('posts/<str:myurl>', views.posts),


    

]
