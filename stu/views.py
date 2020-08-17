from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index_view(request):
    return render(request,'login.html')


def login_view(request):

    uname = request.POST.get('uname','')
    password = request.POST.get('pwd','')

    res = Stu.objects.filter(fname=uname,fpwd=password)
    if res:
        print(res)
        list = []
        for  stu in res:
            dict_stu ={}
            dict_stu['uanme'] = stu.fname
            dict_stu['pwd'] = stu.fpwd
            list.append(dict_stu)

            return HttpResponse(list)
    # if uname == 'gyk' and password == 'jyj':
    #     return HttpResponse('登录成功')

    return HttpResponse('登录失败')


def register_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uname = request.POST.get('uname','')
        upwd = request.POST.get('pwd','')

        student = Stu(fname=uname,fpwd=upwd)

        try:
            student.save()
            return HttpResponse('注册成功')
        except Exception as e:
            return HttpResponse(e)


def show_view(request):
    all_students = Stu.objects.all()

    return render(request,'all_students.html',{'res':all_students})