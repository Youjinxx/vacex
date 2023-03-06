from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')
    #Post를 다 불러오는걸 posts라고 하기로 한다. posts에 post의 모든 객체를 저장한다.    
    return render(
        request,
        'main/index.html',
        {
            'posts':posts,
        }
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        'main/postdetail.html',
        {
            'post':post,
        }
    )

def landing(request):
    posts = Post.objects.all()
    return render(
        request,
        'main/landing.html',
        {
            'posts':posts,
        }
        
    )

def aboutme(request):
    return render(
        request,
        'main/about_me.html'
    )
# Create your views here.
