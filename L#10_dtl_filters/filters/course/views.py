from django.shortcuts import render

# Create your views here.
def c_learn(request):
    c_name = 'python'
    c_details = "this is designed for absolute beginners"
    v_dict={"nm": c_name, "details": c_details}

    return render(request, 'course/course.html', v_dict)