from django import forms

class opinionformulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    sub=forms.CharField(max_length=30)
    autor=forms.CharField(max_length=20)
    cuerpo=forms.CharField(widget=forms.Textarea,max_length=500)
