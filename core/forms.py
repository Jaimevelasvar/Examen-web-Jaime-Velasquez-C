from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    nombre = forms.CharField(max_length=20, help_text="Ingrese su nombre")
    apellido = forms.CharField(max_length=20, help_text="Ingrese su apellido")
    email = forms.EmailField(max_length=100, help_text="Ingrese su correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "nombre", "apellido", "email", "password1", "password2")