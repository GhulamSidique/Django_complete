from django.contrib import admin
from django.urls import path
from fees.views import fees
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fee/', fees)
]