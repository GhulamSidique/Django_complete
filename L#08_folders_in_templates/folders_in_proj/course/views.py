from django.shortcuts import render

# Create your views here.
def learn_cor(request):
    return render(request, 'course/course.html')