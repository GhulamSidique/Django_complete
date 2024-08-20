from django.shortcuts import render
from datetime import datetime
# Create your views here.
def fee(request):
    d=datetime.now()
    dis='the discount for the course will end at'
    return render (request, 'fees/fees.html', {'t': d, 'dis':dis})