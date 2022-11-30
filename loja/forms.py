from django import forms
from django.core import serializers
from django.core.exceptions import ValidationError

from itertools import cycle

from Shopping import settings
from categoria.models import Categoria
from loja.models import Loja


class PesquisaLojaForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False
    )




class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ('nome', 'categoria', 'cnpj', 'data_cadastro', 'descricao', 'imagem')

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if len(cnpj) != 14:
            raise ValidationError("CNPJ Invalido. Verifique e tente novamente!")

        if cnpj in (c * 14 for c in "1234567890"):
            raise ValidationError("CNPJ Invalido. Verifique e tente novamente!")

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                raise ValidationError("CNPJ Invalido. Verifique e tente novamente!")

        return cnpj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages = {'required': 'Campo obrigatório.', 'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['descricao'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['categoria'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset = Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label = 'Selecione a Categoria da Loja'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['data_cadastro'].error_messages = {'required': 'Campo obrigatório', 'invalid': 'Data inválida'}
        self.fields['data_cadastro'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['data_cadastro'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['cnpj'].error_messages = {'required': 'Campo obrigatório', }
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['imagem'].error_messages = {'required': 'Campo obrigatório', 'invalid_image': 'Imagem Inválida'}
        self.fields['imagem'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})
