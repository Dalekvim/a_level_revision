from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class FurtherMathsHomePage(TemplateView):
  template_name = "further_maths/home.html"

  extra_context={
    'title': 'Further Maths Home',
    'heading': 'Further Maths Home Page',
    'sidebar_heading': 'Topics',
  }
  