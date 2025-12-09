from django import forms
from .models import aluno, frequencia

class AlunoForm(forms.ModelForm):
    class Meta:
        model = aluno
        fields = ['nome', 'matricula', 'curso']

class FrequenciaForm(forms.ModelForm):

    data = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "DD/MM/AAAA",  # pode aparecer dependendo do navegador
                "class": "campo-data",
            }
        )
    )

    class Meta:
        model = frequencia
        fields = ['aluno', 'data', 'presente']

