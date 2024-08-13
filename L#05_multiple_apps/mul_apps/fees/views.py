from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cor_fees(request):
    fee='fees for the course is 5k'
    return HttpResponse(fee)