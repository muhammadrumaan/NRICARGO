
from django.db import models
from login_app.models import CredentialsTable
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
# Create your models here.




# class UserTable(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         db_table = 'UserTable'


class ProductTable(models.Model):
    product_id = models.CharField(max_length=100, unique=True, primary_key=True)
    product_name = models.CharField(max_length=100, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.product_id, self.product_name

    class Meta:
        db_table = 'product_table'


class OrderTable(models.Model):
    username = models.ForeignKey(CredentialsTable, related_name='ordered_by', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=30, unique=True, primary_key=True)
    order = models.CharField(max_length=300)

    class Meta:
        db_table = 'order_table'

