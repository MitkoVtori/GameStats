from django import template
from django.contrib.auth import get_user_model


UserModel = get_user_model()
register = template.Library()


@register.filter(name="UserModel")
def user_model(value):
    return UserModel.objects.get(username=value)