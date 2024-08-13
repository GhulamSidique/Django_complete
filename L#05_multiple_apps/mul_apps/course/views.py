from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_cor(request):
    res='<h2> Hello welcome to django complete course </h2>'
    return HttpResponse(res)