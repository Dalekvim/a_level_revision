from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.FurtherMathsHomePage.as_view(), name='further-maths-home'),
  path('proof/', views.ProofsList.as_view(), name='further-maths-proofs'),
  path('proof/<int:pk>/', views.ProofDetails.as_view(), name='proof-detail'),
]