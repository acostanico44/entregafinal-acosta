from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import CustomUserCreationForm, UserForm, ProfileForm
from .models import Profile

# -------------------------
# Signup View (FBV)
# -------------------------
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Crear perfil vacío
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


# -------------------------
# Login View (CBV)
# -------------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


# -------------------------
# Logout View (CBV)
# -------------------------
class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


# -------------------------
# Profile View (FBV)
# -------------------------
@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


# -------------------------
# Edit Profile View (FBV)
# -------------------------
@login_required
def edit_profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

