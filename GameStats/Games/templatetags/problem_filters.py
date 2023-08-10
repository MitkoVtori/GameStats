from django import template


register = template.Library()


@register.filter(name="sort")
def sort_by_date(value):
    return value.order_by("date_reported")
