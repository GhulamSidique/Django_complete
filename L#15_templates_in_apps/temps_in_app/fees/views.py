from django.shortcuts import render

# Create your views here.
def fees(request):
    paid_fees = ['15k', '20k', '15k', 'No', '15k']
    fess_details = 'each student has paid following fees'
    st_dict = {"pf": paid_fees, 'ft': fess_details}

    return render(request, 'fees/fees.html', context=st_dict)