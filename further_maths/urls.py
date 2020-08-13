from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.FurtherMathsHomePage.as_view(), name='further-maths-home'),
  path('proofs/', views.ProofsList.as_view(), name='further-maths-proofs'),
  path('proofs/<int:pk>/', views.ProofDetails.as_view(), name='proof-detail'),
]