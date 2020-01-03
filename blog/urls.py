from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_list.html/', views.post_list1, name='post_list.html'),
]
