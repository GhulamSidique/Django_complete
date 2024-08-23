from django.shortcuts import render
from datetime import datetime
# Create your views here.
def l_course(request):
    c_name='python: '
    c_details = 'this course is for absolutely beginners and will start at '
    s_date=datetime.now()
    c_dict = {'nm':c_name, 'dt':c_details, 'd':s_date}

    return render(request, 'course/course.html', context=c_dict)
