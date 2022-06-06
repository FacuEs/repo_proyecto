from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class alta_alumnos(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    nacimiento = forms.DateField()

class alta_profesores(forms.Form):
    Nombre = forms.CharField(max_length=40)
    legajo = forms.IntegerField()
    