from django import forms
from .models import Tipocaso
class tipocasoform(forms.ModelForm):
    class Meta:
        model = Tipocaso
        fields = ['nombre']
        labels = {'nombre': 'Nombre ',}
        widget = {'nombre': forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
