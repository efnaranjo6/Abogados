from django import forms
from .models import Rol


class rolform(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombreRol']
        labels = {'nombreRol': 'Nombre '}
        widget = {'nombreRol': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
