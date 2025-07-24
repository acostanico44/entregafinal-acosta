# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu perfil fue actualizado con éxito.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, user=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
