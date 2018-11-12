from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dashboard


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class DashboardUpdateForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['image']
