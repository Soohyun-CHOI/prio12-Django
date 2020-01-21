from django.shortcuts import render, redirect
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()
    ctx = {
        "post": qs
    }
    return render(request, "blog/post_list.html", ctx)


def post_read(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        "post": post
    }
    return render(request, "blog/post_read.html", ctx)


def post_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        post = Post.objects.create(title=title, content=content)
        return redirect(f"/blog/{post.pk}")

    return render(request, "blog/post_create.html")