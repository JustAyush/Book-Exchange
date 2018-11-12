from django.shortcuts import render, redirect
from .forms import UserUpdateForm, DashboardUpdateForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from . import forms

# Create your views here.


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
