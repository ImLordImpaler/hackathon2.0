from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from .forms import NewUser
from .models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def like(request , id):
    post = get_object_or_404(Post , id=id)
    liked = False
    if post.liked.filter(id=request.user.id).exists():
        liked = False
        post.liked.remove(request.user)
    else:
        liked = True
        post.liked.add(request.user)
    return redirect('detailedPost', pk=id )

def detailedPost(request , pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')
    print(comments)
    liked = False
    if post.liked.filter(id=request.user.id).exists():
        liked = False
    else:
        liked = True
    
    
    if request.method == 'POST':
        txt = request.POST.get('comment')
        Comment.objects.create(post = post , text = txt , user = request.user)
        return redirect('detailedPost' , pk=pk)

    params = {
        'post': post,
        'liked': liked,
        'comments': comments,
    }
    return render(request,'detailedPost.html' , params)


def index(request):
    posts = Post.objects.all().order_by('-time')
    
    params = {
        'posts' : posts,
        
        }
    return render(request , 'index.html' , params)

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(request , username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('<h1> WHo are you </h1>')
            
    return render(request , 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('index')
        else:
            return redirect('register')
    params = {
        'form':form
    }
    return render(request, 'register.html' , params)

def profile(request ):
    if request.user is not None:
        user = Profile.objects.get(user = request.user)
        print(user)
    else:
        user = None
    params = {
        'user': user
    }
    return render(request , 'profile.html' , params )


def newPost(request):
    if request.method == 'POST':
        post = request.POST.get('post')
        Post.objects.create(user = request.user , txt = post)
        return redirect('index')
    return render(request , 'newPost.html')

def newComment(request , pk):
    post = Post.objects.get(id=pk)

    return redirect('detailed_post' ,pk = pk )