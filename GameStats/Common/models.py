from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db import models
from GameStats.Common.validators import only_letters_numbers_and_underscores


class AppUser(AbstractBaseUser):
    username = models.CharField(max_length=30, validators=[MinLengthValidator(2), only_letters_numbers_and_underscores],
                                unique=True, error_messages={"unique": "User with this username already exists!"})

    USERNAME_FIELD = "username"

    email = models.EmailField(unique=True, error_messages={"unique": "User with this email address already exists!"})

    password = models.CharField(max_length=30, validators=[
        MinLengthValidator(8, message="Password must be at least 8 characters long")
    ])

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    