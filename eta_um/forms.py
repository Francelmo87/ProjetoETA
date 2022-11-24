from django import forms      # importação do formulario do django

from .models import EtaUm      # importando o modelo de Banco de dados


class EtaUmForm(forms.ModelForm):
    # deixar o formato de data escolhida por um calendario
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
        model = EtaUm
        fields = '__all__'
