import markdown
from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    md = markdown.Markdown(extensions=["fenced_code"])
    posts = Post.objects.all().order_by("-created_on")
    for post in posts:
        post.body = md.convert(post.body)
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_detail(request, pk):
    md = markdown.Markdown(extensions=["fenced_code"])
    post = Post.objects.get(pk=pk)
    post.body = md.convert(post.body)
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)