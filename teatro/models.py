from django.db import models



class Teatro(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100)
    imagem = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=300)

    class Meta:
        db_table = 'teatro'

    def __str__(self):
        return self.nome
