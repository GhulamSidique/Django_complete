from django.shortcuts import render

# Create your views here.
def l_course(request):
    st_list = ['ali', 'maha', 'aliya', 'anam', 'khan']
    st_details = 'following is the list of passed students with good grades'
    st_dict = {'list':st_list, 'dt': st_details}
    
    return render(request, 'course/course.html', context=st_dict)