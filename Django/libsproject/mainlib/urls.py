from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authv_views

from . import views as user_views


urlpatterns = [

    path('a/', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout')
    #path('<int:question_id>/', views.details, name='detail'),

]