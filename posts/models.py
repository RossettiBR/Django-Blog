from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os


class Post(models.Model):
    titulo_post = models.CharField(max_length=65, verbose_name='Título')
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data')
    conteudo_post = models.TextField()
    excerto_post = models.TextField()
    categoria_post = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING,
        blank=True, null=True,
        verbose_name='Categoria')
    imagem_post = models.ImageField(
        upload_to='post_img/%Y/%m/%d',
        blank=True, null=True,
        verbose_name='Imagem')
    publicado_post = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self) -> str:
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.tamanho_imagem(self.imagem_post.name, 800)

    @staticmethod
    def tamanho_imagem(nome_image, nova_largura):

        img_path = os.path.join(settings.MEDIA_ROOT, nome_image)
        img = Image.open(img_path)

        widht, height = img.size
        nova_altura = round((nova_largura * height) / widht)

        if widht <= nova_largura:
            img.close()
            return

        nova_imagem = img.resize((nova_largura, nova_altura), Image.ANTIALIAS)

        nova_imagem.save(
            img_path,
            optimize=True,
            quality=60
        )
        nova_imagem.close()
