from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

register = template.Library()

@register.filter(name='mul')
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
