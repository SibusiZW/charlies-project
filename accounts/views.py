from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        usr = request.POST.get('usr')
        pwd = request.POST.get('pwd')

        obj = User.objects.create(email=email, username=usr, password=pwd)
        obj.save()

        return redirect('login')

    return render(request, 'signup.html')