from django import forms      # importação do formulario do django

from .models import EtaCinco      # importando o modelo de Banco de dados


class EtaCincoForm(forms.ModelForm):
    # deixar o formato de data escolhida por um calendário
    data = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date'
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = EtaCinco
        fields = '__all__'
