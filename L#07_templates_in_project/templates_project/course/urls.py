from django.urls import path, include
from . import views

urlpatterns = [
    path('cor/', views.learn_cor),
]
