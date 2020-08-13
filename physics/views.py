from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PhysicsHomePage(TemplateView):
  template_name = "physics/home.html"

  extra_context={
    'title': 'Physics Home',
    'heading': 'Physics Home Page',
    'sidebar_heading': 'Topics',
  }
  