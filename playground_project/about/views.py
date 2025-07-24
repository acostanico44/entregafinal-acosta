# about/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def about_view(request):
    return render(request, 'about/about.html')


# Create your views here.
