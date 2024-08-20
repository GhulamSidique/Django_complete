from django.shortcuts import render

# Create your views here.
def l_course(request):
    c_list = ['py', 'java', 'js', 'ph']
    details = 'this is the list of top popular programming languages'

    return render(request, 'course/course.html', {'list':c_list, 'dt': details})