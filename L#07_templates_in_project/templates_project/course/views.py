from django.shortcuts import render

# Create your views here.
def learn_cor(request):
    # following line of code will render the html file named course.html
    return render(request, 'course.html')