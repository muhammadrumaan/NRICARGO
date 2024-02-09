from django.urls import path
from .views import products_page


urlpatterns = [
    path('products/', products_page)

]