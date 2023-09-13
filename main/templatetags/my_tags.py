from django import template

register = template.Library()

@register.filter
def mediapath(value):
    return f'/media/{value}'


@register.simple_tag
def mediapath(value):
    return f'/media/{value}'
