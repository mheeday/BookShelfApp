from ast import ImportFrom
from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookReview

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('rev',)