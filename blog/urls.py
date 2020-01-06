from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.allblogs, name='allblogs'), #name should be the same as the name of the file. 
    path('<int:blog_id>/', views.blogdetail, name='blogdetail')
    ]