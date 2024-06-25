from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class opinionformulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    sub=forms.CharField(max_length=30)
    autor=forms.CharField(max_length=20)
    cuerpo=forms.CharField(widget=forms.Textarea,max_length=500)

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

    class meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={k:"" for k in fields}