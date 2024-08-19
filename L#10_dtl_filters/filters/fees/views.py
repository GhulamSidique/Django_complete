from django.shortcuts import render

# Create your views here.
def fees(request):
    fees = '2k'
    v_dict = {'fee': fees}

    return render(request, 'fees/fees.html', context=v_dict)