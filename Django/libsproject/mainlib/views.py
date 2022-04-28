from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from . import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    cat_options = {'CO': 'COMIC',
        'FA': 'FANTASY',
        'AC': 'ACTION',
        'TH': 'THRILLER',
        'CN': 'CONTEMPORARY',
    }

    context = {'context_home':[]}

    for i in range(3):
        a = random.choices(list(cat_options.keys()))[0]
        b = random.choice(Books.objects.filter(book_cat=a))
        context['context_home'].append(cat_options[a])
        context['context_home'].append(b)
        context['context_home'].append(f"mainlib/{b.book_cover}.jpg")
        cat_options.pop(a)
    print(context)
    return render(request, 'mainlib/home.html', context)

""" @pass
def user_home(request, username):
    if request.user.is_authenticated:
        #get users last viewed three genre
        #get users last viewed books there
        return render(request, )
    else:
        messages.info(request, f"Please, Login.")
        return redirect('login') """




def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            #forms.UserRegistrationForm.cleaned_data['username']
            form.save()
            
            messages.success(request, f"Welcome {form.cleaned_data['first_name']}!, account created successfully.")
            return redirect('login')

    else:
        form = forms.UserRegistrationForm()

    context = {'form':form}
    return render(request, 'mainlib/register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"Welcome back, {username}.")
                return redirect('home')
            else:
                messages.warning(request, "Invalid Username or Password!")
        else:
            messages.warning(request, "Invalid Username or Password!")
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'mainlib/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('home')

