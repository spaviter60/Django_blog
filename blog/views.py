from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Pavitar Singh',
        'title': 'Get ready',
        'content': 'This is testing blog',
        'date_posted': 'March 6, 2020'
    },
    {
        'author': 'Pavitar Singh',
        'title': 'Get ready part 2',
        'content': 'This is testing 2  blog',
        'date_posted': 'March 6, 2020'
    }

]


def home(request):
     context = {
        'posts': posts
     }
     return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
# Create your views here.
