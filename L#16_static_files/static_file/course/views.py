from django.shortcuts import render

# Create your views here.
def l_course(request):
    c_list = ['java', 'py', 'js', 'php']
    c_rank = [1, 2, 4, 3, 5]
    c_details = 'the courses rank wise are as under;'
    c_dict = {'list':c_list, 'cr':c_rank, 'cd': c_details}

    return render(request, 'course/course.html', context=c_dict)