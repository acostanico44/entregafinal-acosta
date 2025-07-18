from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages_images/', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"


# Create your models here.
