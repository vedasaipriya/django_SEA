from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

'''def home(request):
    return HttpResponse("<h1>Welcome to Django</h1>")
'''

from django.shortcuts import render, redirect

from .models import RegisterStore, Employee


def register(request):
    return render(request, 'register.html')


def login(request):
    uname = request.POST.get('uname')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    user = RegisterStore.objects.create(username=uname, password=password, email=email, mobile=phone)
    user.save()
    return render(request, 'login.html')


def home(request):
    uname = request.POST.get('uname')
    return render(request, 'home.html', {'uname': uname})


def insert_emp(request):

    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        desg = request.POST.get('desg')
        emp = Employee.objects.create(empid=eid, name=ename, gender=gender, email=email, designation=desg)
        emp.save()
        return redirect('/viewall/')

    return render(request, 'insert.html')


def view_all(request):
    emp = Employee.objects.all()
    return render(request, 'display.html', {'employees': emp})


def update_emp(request,pk):
    emp = Employee.objects.get(id=pk)

    if request.method == 'POST':
        emp.empid = request.POST.get('eid')
        emp.name = request.POST.get('ename')
        emp.email = request.POST.get('email')
        emp.gender = request.POST.get('gender')
        emp.designation = request.POST.get('desg')
        emp.save()
        return redirect('/viewall/')

    return render(request, 'update.html',{'employee': emp})


def delete_emp(request,pk):
    emp = Employee.objects.get(id=pk)

    if request.method == 'POST':
        emp.delete()
        return redirect('/viewall/')

    return render(request, 'delete.html',{'employee': emp})
