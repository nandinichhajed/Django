from django.shortcuts import render
from django.views.generic import ListView
from .models import cmdr
# Create your views here.

class HomePageView(ListView):
    model = cmdr
    template_name = 'home.html'