from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ComputerScienceHomePage(TemplateView):
  template_name = "computer_science/home.html"

  extra_context={
    'title': 'Computer Science Home',
    'heading': 'Computer Science Home Page',
    'sidebar_heading': 'Topics',
  }
  