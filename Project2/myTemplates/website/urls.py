from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='HomePage'),
    path('about', views.AboutPageView.as_view(), name='AboutPage'),
    path('contact', views.ContactPageView.as_view(), name='ContactPage'),
]