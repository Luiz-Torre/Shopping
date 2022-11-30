from decimal import Decimal

from carrinho.models import Carrinho
from Shopping import settings


class Carrinho_Function(object):

    def __init__(self, request):
        self.session = request.session
        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)


        if not self.carrinho:

            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

    def atualiza(self, id, quantidade):

        produto = Carrinho.objects.get(id=id)

        if id not in self.carrinho:
            self.carrinho[id] = {'id': id, 'preco': str(produto.preco), 'quantidade': quantidade,
                                 'preco_total': str(produto.preco * quantidade)}
        else:
            self.carrinho[id]['quantidade'] = quantidade
            self.carrinho[id]['preco_total'] = str(self.carrinho[id]['quantidade'] * Decimal(self.carrinho[id]['preco']))

        self.salvar()

    def salvar(self):
        self.session.modified = True

    def remover(self, id):
        if id in self.carrinho:
            del self.carrinho[id]
            self.salvar()


    def get_preco_carrinho(self):
        return sum(Decimal(item['preco_total']) for item in self.carrinho.values())

    def get_quantidade_carrinho(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_produtos(self):
        lista = []
        for item in self.carrinho.values():
            produto = Carrinho.objects.get(id=item['id'])
            lista.append({'produto': produto,
                          'id': item['id'],
                          'preco': Decimal(item['preco']),
                          'quantidade': item['quantidade'],})
        return lista