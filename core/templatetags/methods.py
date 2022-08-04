from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, size):
    return value[0:size]
