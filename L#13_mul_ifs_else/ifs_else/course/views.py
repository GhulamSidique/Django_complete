from django.shortcuts import render

# Create your views here.
def l_course(request):
    c_name='python'
    c_details = "this course is designed for absolutely beginners"

    return render(request, 'course/course.html', {'nm': c_name, 'dt': c_details})