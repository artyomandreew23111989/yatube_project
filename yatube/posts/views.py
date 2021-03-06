from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):    
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = {
        'text': 'Главная страница',
        'title': title
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title': title
    }
    return render(request, template)