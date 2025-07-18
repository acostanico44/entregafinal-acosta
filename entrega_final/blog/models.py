from django.db import models
from ckeditor.fields import RichTextField  # Si usás ckeditor

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()  # o models.TextField()
    imagen = models.ImageField(upload_to='pages/')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Create your models here.
