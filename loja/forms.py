from django import forms
from django.core.validators import RegexValidator

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

        self.fields['cnpj'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['imagem'].error_messages={'required': 'Campo obrigatório', 'invalid_image': 'Imagem Inválida'}
        self.fields['imagem'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})
