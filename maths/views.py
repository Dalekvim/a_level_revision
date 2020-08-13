from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MathsHomePage(TemplateView):
  template_name = "maths/home.html"

  extra_context={
    'title': 'Maths Home',
    'heading': 'Maths Home Page',
    'sidebar_heading': 'Topics',
  }
  