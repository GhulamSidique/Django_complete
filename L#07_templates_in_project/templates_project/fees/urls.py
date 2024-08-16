from django.urls import path, include
from . import views

urlpatterns = [
    path('fee/', views.fees),
]
