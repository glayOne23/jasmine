from django import template

register = template.Library()


@register.filter
def ubah_anyflip_url(value):
    value = value.replace('anyflip.com', 'online.anyflip.com')
    value += 'index.html'
    return value