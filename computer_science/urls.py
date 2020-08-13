from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.ComputerScienceHomePage.as_view(), name='computer-science-home'),
]