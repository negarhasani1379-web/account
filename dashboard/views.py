# from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
class DashboardView(ListView):
    model = User
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'users'