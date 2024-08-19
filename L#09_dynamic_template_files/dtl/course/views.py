from django.shortcuts import render

# Create your views here.
def learn_cor(request):
    c_name="django"
    c_details="learn django and master it with us at nominal price per month"
    vars_dict={'nm':c_name, 'details':c_details}
    return render(request, 'course/course.html',context=vars_dict)