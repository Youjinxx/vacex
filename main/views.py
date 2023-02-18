from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'main/index.html',
        {
            'posts':posts,
        }
    )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'main/postdetail.html',
        {
            'post':post,
        }
    )
# Create your views here.
