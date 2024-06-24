from django import forms

class opinionformulario(forms.Form):
    fecha=forms.DateField()
    titulo=forms.CharField()
    sub=forms.CharField()
    autor=forms.CharField()
    cuerpo=forms.CharField(widget=forms.Textarea)
