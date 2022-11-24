from django import forms      # importação do formulario do django

from .models import Etatres      # importando o modelo de Banco de dados


class EtatresForm(forms.ModelForm):
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
        model = Etatres
        fields = '__all__'
