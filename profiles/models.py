from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(
        upload_to="profile_pictures",
        default="default_profile.jpg",
        blank=True,
        null=True,
    )
    bio = models.TextField(default="This is my bio", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
