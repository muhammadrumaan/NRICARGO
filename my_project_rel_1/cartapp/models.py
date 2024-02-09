"""
cartapp/models.py
"""

from django.db import models
from login_app.models import CredentialsTable
# from login_app.models import UserTable
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserTable(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         db_table = 'UserTable'


# Create your models here.
class ShippingTable(models.Model):
    order_id = models.CharField(max_length=100, unique=True, primary_key= True)
    shipping_address = models.CharField(max_length=300)
    username = models.ForeignKey(CredentialsTable,related_name="ship_to", on_delete=models.CASCADE)
    def __str__(self):
        return self.order_id
    class Meta:
        db_table= "ShippingTable"
