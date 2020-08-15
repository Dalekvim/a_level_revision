from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.
class FurtherMathsHomePage(TemplateView):
  template_name = "further_maths/home.html"

  extra_context = {
    'title': 'Further Maths Home',
    'heading': 'Further Maths Home Page',
    'sidebar_heading': 'Topics',
  }
  
class ProofsList(ListView):
  model = models.Proof

  extra_context = {
    'title': 'Proofs',
    'heading': 'Mathematical Proofs',
    'sidebar_heading': 'Helpful Links',
  }

class ProofDetails(DetailView):
  model = models.Proof

  extra_context = {
    'title': 'Detailed View',
    'heading': 'Proof in Detail',
    'sidebar_heading': 'You are Currently in Detailed View',
  }