from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 carateres como maximo y tambien debe ser valido')

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}