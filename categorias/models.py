from django.db import models


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=65, verbose_name='Nome')

    def __str__(self) -> str:
        return self.nome_cat
