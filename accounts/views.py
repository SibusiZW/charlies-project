from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')

        userr = authenticate(request, username=usr, password=pwd)

        if userr:
            login(request, userr)
            return HttpResponse('Logged In')
        else:
            return HttpResponse('Incorrect username/password!')

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')

        obj = User.objects.create_user(email=email, username=usr, password=pwd)
        obj.save()

        return redirect('login')

    return render(request, 'signup.html')