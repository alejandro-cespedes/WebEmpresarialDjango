from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service 
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'contact__input', 'placeholder': 'Ingresa el titulo:'}),
            'subtitle': forms.EmailInput(attrs={'class': 'contact__input', 'placeholder': 'Ingresa el subtitulo:'}),
            'content': forms.Textarea(attrs={'class': 'contact__input contact__input--area', 'placeholder': 'Contenido...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'contact__input'}),
        }
        labels = {
            'title':'','subtitle': '', 'content': '', 'image': ''
        }
