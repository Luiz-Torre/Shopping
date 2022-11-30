from django.db import models

from categoria.models import Categoria


class Carrinho(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='lojas', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    models.SlugField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits =10, decimal_places = 2)

    class Meta:
        db_table = 'carrinho'

    def __str__(self):
        return self.nome
