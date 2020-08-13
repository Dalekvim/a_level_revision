from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.PhysicsHomePage.as_view(), name='physics-home'),
]