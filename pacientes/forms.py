from django.forms import ModelForm
from .models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'idade', 'peso', 'bio', 'photo']