from django.shortcuts import render
from datetime import datetime

# Create your views here.
def cor1(request):
    c_name = 'python'
    c_details = 'You can enroll in this course till'
    c_date= datetime.now()
    c_dict = {'nm':c_name, 'dt': c_details, 'd': c_date}

    return render(request, 'course/course1.html', context=c_dict)

def cor2(request):
    c_name2 = 'java'
    c_details = 'You can enroll in this course till'
    c_date= datetime.now()
    c_dict2 = {'nm2':c_name2, 'dt': c_details, 'd': c_date}

    return render(request, 'course/course2.html', context=c_dict2)

def home(request):
    return render(request, 'course/home.html')