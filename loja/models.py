from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from categoria.models import Categoria


class Loja(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='lojas', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique = True)
    slug = models.SlugField(max_length=100)
    imagem = models.ImageField(upload_to='images/')
    descricao = models.CharField(max_length=300)
    cnpj = models.CharField(max_length=14)
    data_cadastro = models.DateField()


    class Meta:
        db_table='loja'


    def __str__(self):
        return self.nome