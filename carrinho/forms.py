from django import forms
from carrinho.models import Carrinho
from categoria.models import Categoria



class CarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ('nome', 'categoria', 'quantidade', 'preco')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages = {'required': 'Campo obrigatório.', 'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['categoria'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset = Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label = 'Selecione a Categoria do Produto'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-sm'})


        self.fields['quantidade'].error_messages = {'required': 'Campo obrigatório', }
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['preco'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['preco'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})



class QuantidadeForm(forms.Form):

    produto_id = forms.CharField(widget=forms.HiddenInput())

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control-sm quantidade ',
                                      'style': 'text-align: center;  width: 70px;',
                                      'onkeypress': 'return (event.charCode>=48 && event.charCode <=57'
                                      }),
        required=True
    )
