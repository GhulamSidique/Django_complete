from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees(request):
    return HttpResponse("the course fees is 5k")