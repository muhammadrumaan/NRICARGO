"""
cartapp/urls.py
"""

from django.urls import path
from .views import my_cart_page
# from .views import my_checkout_page

urlpatterns = [
    path('',my_cart_page),
    path('cart/',my_cart_page),
    # path('checkout/',my_checkout_page),
]

# http://127.0.0.1:8000/my_cart_page
