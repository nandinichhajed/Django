from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('vrform', views.vrform, name='vrform'), 
]
