from django.urls import path
from . import views

urlpatterns = [
    path('cor1/', views.l_course1),
    path('cor2/', views.l_course2),
]
