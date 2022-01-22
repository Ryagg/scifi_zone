from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_vat')
def calc_vat(items_sum, percentage):
    vat = items_sum - (items_sum * percentage)
    return vat
