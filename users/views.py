from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Users

class UsersListView(ListView):
    model = Users
    template_name = "users/index.html"
    context_object_name = 'users'
    ordering = ['-date_created']

class UserCreateView(CreateView):
    model = Users
    fields = ['name']
    template_name = "users/create.html"
    success_url = "../users"