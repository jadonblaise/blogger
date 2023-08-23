from django.urls import path
from .views import home, blog_list, blog_detail, author_detail

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),

]