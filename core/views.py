from django.shortcuts import render, redirect, get_object_or_404
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

@login_required(login_url='/auth/login')
def details_view(request, pk):

    hack = get_object_or_404(Hack, pk=pk)

    return render(request, 'details.html', { 'hack': hack })

@login_required(login_url='/auth/login')
def my_hacks(request):
    hacks = Hack.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'hacks.html', { 'hacks': hacks })

@login_required(login_url='/auth/login')
def delete_hack(request, pk):
    obj = get_object_or_404(Hack, pk=pk)
    obj.delete()

    return redirect('home')

@login_required(login_url='/auth/login')
def create_hack(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        obj = Hack.objects.create(title=title, description=desc, user=request.user)
        obj.save()
        return redirect('home')

    return render(request, 'create_hack.html')