from django.urls import path
from . import views
urlpatterns = [
    path('fee/', views.fees)
]