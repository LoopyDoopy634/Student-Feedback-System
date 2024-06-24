from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
