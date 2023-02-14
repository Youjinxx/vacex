from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'main/index.html',
        {
            'posts':posts,
        }
    )
# Create your views here.
