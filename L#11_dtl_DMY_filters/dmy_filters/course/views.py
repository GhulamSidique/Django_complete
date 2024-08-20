from django.shortcuts import render
from datetime import datetime
# Create your views here.
def l_course(request):
    d=datetime.now()
    return render(request, 'course/course.html',{'nm':'java', 'dt':d})
