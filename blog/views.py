import makrdown
from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.body = md.converter(post.body)
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)