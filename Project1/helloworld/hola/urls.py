from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.helloPage, name="helloPage")
]