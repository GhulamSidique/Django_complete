from django.urls import path
from . import views
urlpatterns = [
    path('cor/', views.learn_cor),
]