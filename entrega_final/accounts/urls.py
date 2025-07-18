# accounts/urls.py
from django.urls import path
from .views import CustomLogoutView

urlpatterns = [
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView,
    signup_view, profile_view, edit_profile_view
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
]
