from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import (LoginView,LogoutView)
from django.views.generic import CreateView
from .forms import SignupForm
class SignupView(CreateView):

    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
class CustomLogoutView(LogoutView):
    next_page = 'login'

class CustomLoginView(LoginView):

    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):

    next_page = 'login'

