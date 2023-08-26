from django import forms


class Contacto(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=50)
    mensaje = forms.Textarea()

class correo(forms.Form):
    correo = forms.EmailField()
    
