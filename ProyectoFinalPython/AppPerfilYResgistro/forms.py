from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from AppProyectoFinalPython.models import Avatar


class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:""for k in fields}

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))    
    email = forms.CharField(label="Correo Electrónico", widget=forms.TextInput(attrs={'class': 'form-control'}))    
    first_name = forms.CharField(label="Nombres", widget=forms.TextInput(attrs={'class': 'form-control'}))    
    last_name = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={'class': 'form-control'}))    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden..")
        return password2


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)