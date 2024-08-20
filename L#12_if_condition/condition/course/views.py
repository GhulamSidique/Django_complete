from django.shortcuts import render

# Create your views here.
def l_course(request):
    c_name='java'
    c_details = 'hello! Welcome to the world of '
    return render(request, 'course/course.html', {'nm': c_name, 'dt': c_details})