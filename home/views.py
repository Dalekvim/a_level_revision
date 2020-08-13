from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
  template_name = "home/home.html"

  extra_context={
    'title': 'Home',
    'heading': 'Home Page',
    'sidebar_heading': 'About the Creator',
  }
  