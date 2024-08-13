from django.contrib import admin
from django.urls import path
from course.views import cor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', cor)
]