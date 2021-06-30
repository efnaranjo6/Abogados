from django import forms
from .models import Detalleusuario


class detalleusuarioform(forms.ModelForm):
    class Meta:
        model = Detalleusuario
        fields = ['Rol', 'usuario']
        labels = {
                  'Rol': 'Seleccione un rol ',
                  'usuario': 'Seleccione un usuario '
                  }
        widget = {
                  'Rol': forms.TextInput(),
                  'usuario': forms.TextInput(),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
