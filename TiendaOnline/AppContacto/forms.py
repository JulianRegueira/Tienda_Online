from django import forms

class Formulario_Contacto(forms.Form):

    asunto=forms.CharField(label="Asunto", required=True)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="Contenido", required=True, widget=forms.Textarea)