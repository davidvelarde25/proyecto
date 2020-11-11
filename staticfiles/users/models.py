from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# table roles
class Rol(models.Model):
    Description = models.CharField(max_length=250, null=False)
    def __str__(self):
        return self.Description

# tabla profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    rol = models.OneToOneField(Rol, on_delete=models.PROTECT)
