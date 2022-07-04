from django import template

register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios):
    return f'{num_comentarios} COMENTÁRIO(S)'
