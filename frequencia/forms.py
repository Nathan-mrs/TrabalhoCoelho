from django import forms
from .models import aluno, frequencia

class AlunoForm(forms.ModelForm):
    class Meta:
        model = aluno
        fields = ['nome', 'matricula', 'curso']

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = frequencia
        fields = ['aluno', 'data', 'presente']
