from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/auth/login')
def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('login')