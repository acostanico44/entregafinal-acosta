# blog/forms.py
from django import forms
from .models import Post
from .models import Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribí tu comentario...',
                'rows': 3
            })
        }