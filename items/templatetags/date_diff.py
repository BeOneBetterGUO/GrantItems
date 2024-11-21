from django import template
from datetime import date

register = template.Library()

@register.filter
def date_diff(value, arg):
    if isinstance(value, date) and isinstance(arg, date):
        return (value - arg).days
    return ''