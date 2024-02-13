from django.urls import path
from .views import products_page, save_cart


urlpatterns = [
    path('products/', products_page),
    path('products/save_cart/', save_cart)

]