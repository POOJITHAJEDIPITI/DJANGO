from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
# password field
    password = models.CharField(max_length=8, blank=False, null=False)
