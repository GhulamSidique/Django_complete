from django.shortcuts import render

# Create your views here.
def fees(request):
    c_fee="2k per month"
    v_dict={'fee': c_fee}
    return render(request, 'fees/fees.html',context=v_dict)