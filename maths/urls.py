from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.MathsHomePage.as_view(), name='maths-home'),
]