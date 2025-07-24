# blog/models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    post = models.ForeignKey('Post', related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario por {self.autor.username} en {self.post.titulo}'

