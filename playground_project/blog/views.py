# blog/views.py
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Post, Comentario
from .forms import PostForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .forms import ComentarioForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        orden = self.request.GET.get('orden', '-fecha_publicacion')
        return Post.objects.all().order_by(orden)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.order_by('-fecha')
    form = ComentarioForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post
                comentario.autor = request.user
                comentario.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')
    def test_func(self):
        return self.request.user == self.get_object().autor

class PostDeleteView(LoginRequiredMixin, DeleteView,UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    def test_func(self):
        return self.request.user == self.get_object().autor

# Vista común con decorador para mostrar mensaje si no hay posts
@login_required
def post_empty_view(request):
    posts = Post.objects.all()
    if not posts:
        mensaje = "No hay páginas aún"
    else:
        mensaje = None
    return render(request, 'blog/post_empty.html', {'mensaje': mensaje})

def home_view(request):
    latest_posts = Post.objects.order_by('-fecha_publicacion')[:3]

    return render(request, 'blog/home.html', {'latest_posts': latest_posts})

# Create your views here.
