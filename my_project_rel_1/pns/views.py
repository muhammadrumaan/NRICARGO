from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ProductTable
import json
import requests

from cartapp.views import my_cart_page


def products_page(request):
    products = ProductTable.objects.all()
    return render(request, 'pns/products.html', {'products': products})


def save_cart(request):
    if request.method == 'POST':
        cart_data_json = request.POST.get('cart_data')
        product_info = json.loads(cart_data_json)
        # Process cart data as needed
        print(product_info)
        print(type(product_info))
        response = requests.post('http://127.0.0.1:8000/cart/', data=product_info)
        # return HttpResponse('Cart data received successfully')
        return HttpResponse(response.content)
    else:
        return HttpResponse('Invalid request method')