from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreatedForm
from .forms import UserUpdateForm, DashboardUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreatedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login');
    else:
        form = UserCreatedForm()
    return render(request, 'users/register.html', {'form': form})

def dashboard(request):
    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        dashboard_update = DashboardUpdateForm(request.POST, request.FILES, instance=request.user.dashboard)
        if user_update.is_valid() and dashboard_update.is_valid():
            user_update.save()
            dashboard_update.save()
            return redirect('dashboard')
    else:
        user_update = UserUpdateForm()
        dashboard_update = DashboardUpdateForm()
    context = {
        'user_update' : user_update,
        'dashboard_update' : dashboard_update
    }

    return render(request, 'users/dashboard.html', context)
