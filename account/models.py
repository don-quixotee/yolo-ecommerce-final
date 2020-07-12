from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    FullName = models.CharField(max_length=130)
    email = models.EmailField(unique = True)
    age = models.PositiveIntegerField(blank=True, null=True)

    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('profile', args=[self.id])
