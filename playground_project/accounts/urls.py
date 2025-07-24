from django.urls import path
from .views import profile_view, edit_profile_view, signup_view
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin

class CustomPasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = '/accounts/profile/'
    success_message = "Tu contraseña fue actualizada con éxito."

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/editar/', edit_profile_view, name='edit_profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='password_change'),
]

