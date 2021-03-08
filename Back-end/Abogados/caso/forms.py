from django import forms
from .models import Caso


class casoform(forms.ModelForm):
    class Meta:
        model = Caso
        fields = ['Persona','Tipocaso', 'Estado']
        labels = {'Tipocaso': 'Seleccione la persona ',
                  'Tipocaso': 'Tido del caso ',
                  'Estado': 'Estado '
                 }
        widget = {'Persona': forms.TextInput(),
                  'Tipocaso': forms.TextInput(),
                  'Estado': forms.TextInput()
                  }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
