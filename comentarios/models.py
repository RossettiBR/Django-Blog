from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=65, verbose_name='Nome')
    email_comentario = models.EmailField(max_length=65, verbose_name='E-mail')
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING,
        blank=True, null=True,
        verbose_name='Usuário')
    data_comentario = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self) -> str:
        return self.nome_comentario
