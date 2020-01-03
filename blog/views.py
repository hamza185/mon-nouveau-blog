from django.shortcuts import render
from django.utils import timezone
from .models import *

def post_list(request):
    name="hamza"
    return render(request, 'blog/index.html', {'name': name})

def post_list1(request):
    name="hamza"
    return render(request, 'blog/post_list.html', {'name': name})
