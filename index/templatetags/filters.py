from datetime import timedelta, datetime

from django import template

register = template.Library()


@register.filter
def check_tag(value, array):
    for i in array:
        if i.title == value:
            return True
    return False

