"""
cartapp/models.py
"""

from django.db import models
# from login_app.models import CredentialsTable

# Create your models here.
class ShippingTable(models.Model):
    order_id = models.AutoField(primary_key=True) #autogenerate
    shipping_address = models.CharField(max_length=300) #from user
    # user = models.ForeignKey(CredentialsTable, related_name="ship_to", on_delete=models.CASCADE) #from session
    user_id = models.IntegerField()
    def __str__(self):
        return self.shipping_address

    class Meta:
        db_table = "ShippingTable"
