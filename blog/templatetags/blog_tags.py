from django import template

register = template.Library()

# Создание фильтра
@register.filter()
def blog_media(path):
    if path:
        return f'/media/{path}'
    return '#'

#http://127.0.0.1:8000/media/photo/blog/caesar_cctaqYW.png