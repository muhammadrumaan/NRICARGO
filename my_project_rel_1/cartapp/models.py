"""
cartapp/models.py
"""

from django.db import models
from login_app.models import CredentialsTable

# Create your models here.
class ShippingTable(models.Model):
    order_id = models.CharField(max_length=100, unique=True, primary_key=True)
    shipping_address = models.CharField(max_length=300)
    user = models.ForeignKey(CredentialsTable, related_name="ship_to", on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = "ShippingTable"
