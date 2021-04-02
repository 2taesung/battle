from django.shortcuts import render, redirect
from .models import Head, Comment, Community

# Create your views here.
def home(request):
    heads = Head.objects.all()
    comments = Comment.objects.all()
    
    # print(heads)
    context ={
        'heads': heads,
        'comments': comments,
    }
    return render(request, 'articles/home.html', context)

def right(request):
    communities = Community.objects.all()
    context = {
        'communities': communities,
    }
    return render(request, 'articles/right.html', context)

def left(request):
    return render(request, 'articles/left.html')