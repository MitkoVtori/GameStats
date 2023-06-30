from django.core.validators import MinLengthValidator
from django.db import models
from GameStats.Games.validators import image_size


class Game(models.Model):
    image = models.ImageField(upload_to="images", validators=[image_size])

    title = models.CharField(max_length=25, validators=[MinLengthValidator(
        2, message="game title must be at least 2 characters long!"
    )], unique=True, error_messages={"unique": "Game with this name already exists!"})

    genre = models.CharField(max_length=10, choices=[
        ("Action", "Action"),
        ("Sports", "Sports"),
        ("Adventure", "Adventure"),
        ("Role-play", "Role-play"),
        ("Racing", "Racing"),
        ("Other", "Other")
    ])

    description = models.TextField(max_length=500)

    creator = models.CharField() # request.user

