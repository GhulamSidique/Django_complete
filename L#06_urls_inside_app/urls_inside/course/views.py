from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cor(request):
    return HttpResponse("this is the python course")