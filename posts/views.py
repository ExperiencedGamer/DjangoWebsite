from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.forms import RegistrationForm
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    #return HttpResponse('Hello From POSTS')
    return render(request, 'posts/index.html', context)

def details(requests, id):
    post = Posts.objects.get(id=id)
    context = {
        'posts': post
    }

    return render(requests, 'posts/details.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    args = {'form' : form}
    return render(request, 'posts/reg_form.html', args)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'posts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')    