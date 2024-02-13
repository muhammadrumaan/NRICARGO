from django.contrib import admin
from .models import ProductTable
from .models import OrderTable

# Register your models here.

admin.site.register(ProductTable)
admin.site.register(OrderTable)
