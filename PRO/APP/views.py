from django.shortcuts import render
from APP.models import BasicInfo, Marks
# Create your views here.


def first(request):
    info_list = BasicInfo.objects.order_by('roll_no')
    mark_list = Marks.objects.order_by('name')
    dict = {'basic_info':info_list, 'marks_info':mark_list}
    return render(request,'first_app.html',context=dict)
