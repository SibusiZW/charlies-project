from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Hack

@login_required(login_url='/auth/login')
def home_view(request):
    hacks = Hack.objects.all().order_by('-created_at')

    return render(request, 'home.html', { 'user': request.user, 'hacks': hacks })

@login_required(login_url='/auth/login')
def signout(request):
    logout(request)
    return redirect('login')