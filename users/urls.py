from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('users', views.UsersListView.as_view(), name='index'),
    path('users/create', views.UserCreateView.as_view(), name='create'),
]
