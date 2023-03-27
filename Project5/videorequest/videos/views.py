from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    if request.method == 'POST':
        # forms VideoForm
        form = VideoForm(request.POST)
        
        if form.is_valid():
            # models - fieldName_in_models - fieldName_in_forms
            new_req = Video(videotitle=request.POST['video_name'], 
                            videodesc=request.POST['video_desc'])
            new_req.save()
            return redirect('index')
    else:
        form = VideoForm()
    context = {'form': form}
    
    return render(request, 'videorequest/vrform.html', context)