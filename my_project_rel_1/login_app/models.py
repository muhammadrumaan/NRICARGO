"""
login_app/models.py
"""

# from django.contrib.auth.models import AbstractUser
from django.db import models

class CredentialsTable(models.Model):
    # You can add custom fields or methods here if needed
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    mobile = models.DecimalField(max_digits=10, decimal_places=0)
    country = models.CharField(max_length=15)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'credentials_table'



