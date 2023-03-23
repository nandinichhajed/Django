from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    return render(request, 'videorequest/vrform.html')