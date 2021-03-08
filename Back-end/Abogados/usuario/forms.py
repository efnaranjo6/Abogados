from django import forms
from usuario.models import usuario


class usuarioform(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['correoUsuario', 'contrasenaUsuario', 'Persona']
        labels = {'correoUsuario ': 'ingrese el  correo ',
                  'contrasenaUsuario ': 'ingrese el  contraseña',
                  'Persona ': 'seleccione la persona'

                  }
        widget = {'correoUsuario': forms.TextInput(),
                  'contrasenaUsuario': forms.TextInput(),
                  'Persona': forms.TextInput(),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
