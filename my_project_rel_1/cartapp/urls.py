"""
cartapp/urls.py
"""

from django.urls import path
from .views import my_cart_page
from .views import back_to_shop
from .views import save_shipping_address
from .views import checkout


urlpatterns = [
    path('',my_cart_page, name='my_cart_page'),
    path('delivery/', save_shipping_address),
    path('back_to_shop/', back_to_shop, name='back_to_shop'),
    path('checkout/',checkout,name= 'checkout')
]

# http://127.0.0.1:8000/cart
