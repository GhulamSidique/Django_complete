from django.shortcuts import render
from datetime import datetime
# Create your views here.
def fees(request):
    fees=1000
    details= 'the course fees is '
    d=datetime.now()

    return render(request, 'fees/fees.html', {'fee': fees, 'dt': details, 'd': d})
