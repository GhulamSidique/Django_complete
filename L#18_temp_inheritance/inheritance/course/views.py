from django.shortcuts import render
from datetime import datetime

# Create your views here.
def l_course1(request):
    c_name = 'python'
    c_details = 'the course will start at'
    c_date=datetime.now()
    c_dict = {'nm': c_name, 'dt':c_details, 'd':c_date}

    return render(request, 'course/course1.html', context=c_dict)

def l_course2(request):
    c_name_2 = 'java'
    c_details_2 = 'the course will start at'
    c_date_2=datetime.now()
    c_dict_2 = {'nm2': c_name_2, 'dt':c_details_2, 'd':c_date_2}

    return render(request, 'course/course2.html', context=c_dict_2)