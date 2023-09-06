from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

'''def home(request):
    return HttpResponse("<h1>Welcome to Django</h1>")
'''

from django.shortcuts import render

from .models import LoginStore


@csrf_exempt
def home(request):
    uname = request.POST['uname']
    password = request.POST['pwd']
    user = LoginStore.objects.create(username=uname, password=password)
    user.save();
    return render(request, 'home.html', {'name': uname})


def login(request):
    return render(request, 'login.html')
