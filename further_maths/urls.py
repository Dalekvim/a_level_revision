from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.FurtherMathsHomePage.as_view(), name='further-maths-home'),
]