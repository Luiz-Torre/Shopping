from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from loja.models import Loja


class Produto(models.Model):
    # categoria = models.ForeignKey(Loja, related_name='loja', on_delete=models.DO_NOTHING)
    # nome = models.CharField(max_length=50, db_index=True, unique=True)
    # telefone = models.IntegerField(max_length=13, db_index=True, unique=True)
    # endereço = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(15)])
    # cnpj = models.IntegerField()

    class Meta:
        db_table='pedido'

    def __str__(self):
        return self.nome