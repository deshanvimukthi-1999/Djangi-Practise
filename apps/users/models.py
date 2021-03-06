from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    owner = models.OneToOneField(
        'users.User', related_name='managing_company', on_delete=models.CASCADE, null=True, blank=True)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.ForeignKey(
        Company, related_name='company_user', on_delete=models.DO_NOTHING)
