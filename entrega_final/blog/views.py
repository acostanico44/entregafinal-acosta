from django.shortcuts import render
from .models import Page 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})
# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

# VISTA LISTA
class PageListView(ListView):
    model = Page
    template_name = 'blog/page_list.html'
    context_object_name = 'pages'

# VISTA DETALLE
class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

# VISTA CREAR
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'blog/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image', 'created_at']
    success_url = reverse_lazy('page_list')

# VISTA EDITAR
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'blog/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image', 'created_at']
    success_url = reverse_lazy('page_list')

# VISTA BORRAR
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')
