from django.core.validators import ValidationError


def only_letters_numbers_and_underscores(value):
    for char in value:
        if not char.isalnum() and char != "_":
            raise ValidationError("The username can contain only of letters, numbers and underscores.")

