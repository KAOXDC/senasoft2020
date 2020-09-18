from django import forms

class contacto_form(forms.Form):
    nombre      = forms.CharField(widget = forms.TextInput())
    #correo      = forms.EmailField()
    mensaje     = forms.CharField(widget = forms.Textarea())


    