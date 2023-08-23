from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Author, Entry

# Create your views here.
def home(request):
    return HttpResponse('Welcome to my blog')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    entries = Entry.objects.filter(blog=blog)
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'entries': entries})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    entries = Entry.objects.filter(author=author)
    return render(request, 'blog/author_detail.html', {'author': author, 'entries': entries})
