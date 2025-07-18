from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

class PageListView(ListView):
    model = Page
    template_name = 'mi_blog/page_list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            return []
        return queryset

class PageDetailView(DetailView):
    model = Page
    template_name = 'mi_blog/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'mi_blog/page_form.html'
    success_url = reverse_lazy('page-list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'mi_blog/page_form.html'
    success_url = reverse_lazy('page-list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'mi_blog/page_confirm_delete.html'
    success_url = reverse_lazy('page-list')

