from django.db import models

from categoria.models import Categoria
from genero_filme.models import GeneroFilme


class Filme(models.Model):
    genero = models.ForeignKey(GeneroFilme, related_name='filmes', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100)
    imagem = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=300)
    data_lancamento = models.DateField()

    class Meta:
        db_table = 'filme'

    def __str__(self):
        return self.nome
