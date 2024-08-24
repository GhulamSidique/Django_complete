from django.urls import path
from . import views
urlpatterns = [
    path('cor1/', views.cor1),
    path('cor2/', views.cor2),
    path('home/', views.home),
]
