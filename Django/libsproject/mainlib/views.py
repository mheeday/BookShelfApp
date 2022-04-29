from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from . import forms
from .models import Books, UserBook, BookReview
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
cate_options = ['Comic', 'Fantasy', 'Action', 'Thriller', 'Contemporary']

def get_random_books(each_cat):
    cat_options = cate_options.copy()
    context = {'context_home':[]}

    for i in range(3):
        key = random.choices(cat_options)[0]
        context['context_home'].append(key)
        print(key)
        books_to_choose = Books.objects.filter(book_cat=key)
        for j in range(each_cat):
            b = random.choice(books_to_choose)
            book_code = b.book_cover
            context['context_home'].append(b)
            books_to_choose = books_to_choose.exclude(book_cover=book_code)
        cat_options.remove(key)

    return context

def home(request):
    context = get_random_books(1)
    if request.user.is_authenticated:
        return redirect('user_home', username=request.user.username)
    return render(request, 'mainlib/home.html', context)

@login_required
def user_home(request, username):
    if request.user.is_authenticated:
        if UserBook.objects.filter(user=request.user).exists():
            context = get_random_books(3)
            return render(request, 'mainlib/user_home.html', context)
        else:
            context = get_random_books(3)
            return render(request, 'mainlib/user_home.html', context)
            
        #get users last viewed three genre
        #get users last viewed books there
            return render(request, 'mainlib/user_home.html', context)
    else:
        messages.info(request, f"Please, Login.")
        return redirect('login')

def book_cat_list(request, category):

    category = category.capitalize()
    books = Books.objects.filter(book_cat=category)
    context = {'context_text':[], 'category':category}
    for book in books:
        context['context_text'].append(book)
    print(context)
    return render(request, 'mainlib/book_cat_list.html', context)

def per_book(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    context = {'book': book}

    book_reviews = BookReview.objects.filter(book_id=book_id).order_by('-date_posted')
    if book_reviews.exists():
        context = {'book': book, 'reviews': book_reviews}
    return render(request, 'mainlib/each_book.html', context)


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
                print(f" Current User ||||||||| {request.user.email}")
                return redirect('user_home', username)
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

