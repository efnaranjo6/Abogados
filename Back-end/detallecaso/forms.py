from django import forms
from .models import Detallecaso


class detallecasoform(forms.ModelForm):
    class Meta:
        model = Detallecaso
        fields = ['descripccion', 'porcentaje', 'Caso']
        labels = {'correoUsuario ': 'ingrese la  descripccion ',
                  'porcentaje ': 'ingrese el  porcentaje',
                  'Caso ': 'seleccione el caso'
                  }
        widget = {'correoUsuario': forms.TextInput(),
                  'porcentaje': forms.TextInput(),
                  'Caso': forms.TextInput()
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if (field=='usuario'):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'})
                self.fields[field].widget.attrs.update({'id': 'id_user'})

            else:                    
                self.fields[field].widget.attrs.update({'class': 'form-control'})
