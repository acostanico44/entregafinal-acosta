from django.db import models
from ckeditor.fields import RichTextField 

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()  
    imagen = models.ImageField(upload_to='pages/')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Create your models here.
