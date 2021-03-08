from django import forms
from .models import Detalleusuario


class detalleusuarioform(forms.ModelForm):
    class Meta:
        model = Detalleusuario
        fields = ['usuario', 'Rol']
        labels = {'usuario': 'Seleccione la persona ',
                  'Rol': 'Seleccione un rol ',
                
                  }
        widget = {'usuario': forms.TextInput(),
                  'Rol': forms.TextInput(),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
