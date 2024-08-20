from django.shortcuts import render

# Create your views here.
def fees(request):
    c_charges=2000
    c_details = 'we charge for this course RS: '
    return render(request, 'fees/fees.html', {"fee": c_charges, "dt": c_details})