from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(blank=True, max_length=32)
    phone = models.CharField(blank=True, max_length=32)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ('user',)
