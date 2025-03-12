from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    TYPE_CHOICES = [
        ('001', _('Admin')),
        ('002', _('Manager')),
        ('003', _('Member')),
    ]
    GENDER_CHOICES = [
        ('m', _('Male')),
        ('f', _('Female')),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='003')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'users_user'