from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from . import forms

# Create your views here.
from django.shortcuts import  render



def post_list(request):
    posts = Post.objects.all().order_by('-date')
    # return HttpResponse("Hello, world. You're at the Home page.")
    return render(request, 'posts/post_list.html',{ 'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'post': post})

@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')

    else:
        form=forms.CreatePost()
        return render(request,'posts/post_new.html',{'form':form})
