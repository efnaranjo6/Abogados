from django import forms
from .models import Detalleusuario


class detalleusuarioform(forms.ModelForm):
    class Meta:
        model = Detalleusuario
        fields = ['Rol',]
        labels = {
                  'Rol': 'Seleccione un rol ',
                  }
        widget = {
                  'Rol': forms.TextInput(),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
