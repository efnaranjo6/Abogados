from django import forms
from .models import Persona


class personaform(forms.ModelForm):
    class Meta:
        model = Persona 
        fields = ['nombrePersona', 'apellidoPersona', 'cedulaPersona']
        labels = {'nombrePersona': 'Nombre ',
                  'apellidoPersona': 'Apellido ',
                  'cedulaPersona': 'Cedula '
                  }
        widget = {'nombrePersona': forms.TextInput(),
                  'apellidoPersona': forms.TextInput(),
                  'cedulaPersona': forms.TextInput(),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
