
"""
cartapp/views.py
"""
import os
from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from pns.models import ProductTable as pt
from .models import ShippingTable
from django.http import JsonResponse
from django.shortcuts import redirect
import json

def back_to_shop(request):
    return redirect('/pns/products/')

def checkout(request):
   return render(request,'orderplaced.html',{})


# def my_cart_page(request):
#     # Get the raw JSON data from the request body
#     try:
#         data = json.loads(request.body)
#         products_info = data.POST
#     except json.JSONDecodeError:
#         products_info = {}
#
#     products = []
#
#     total_items = 0  # Initialize total items counter
#     total_price = 0  # Initialize total price accumulator
#
#     for product_name, quantity in products_info.items():
#         # Find the product in the database
#         try:
#             product = pt.objects.get(name=product_name)
#         except pt.DoesNotExist:
#             # Handle case when product is not found
#             continue
#
#         # Get the image name from the product
#         image_name = product.product_name #this is the name in the database
#         # Construct the path to the product image
#         image_path = os.path.join(settings.BASE_DIR, 'static', 'images', image_name)
#         # Save the image to the product_image folder
#         # You need to implement this part
#
#         # Retrieve the price of the product
#         price = product.product_price
#
#         # Retrieve user_id from session
#         # user_id = request.session.get('user_id')
#         user_id = 1
#
#         # Increment total_items by the quantity of the current product
#         total_items += quantity
#
#         # Calculate the total price of the current product and add it to total_price
#         total_price += price * quantity
#
#         # Construct a dictionary containing product information
#         product_data = {
#             'user_id': user_id,
#             'image_path': image_path,
#             'quantity': quantity,
#             'price': price * quantity,
#         }
#         products.append(product_data)
#
#         # Render the cart page with information about all products
#     context = {
#         'products': products,
#         'total_items': total_items,  # Include total items in the context
#         'total_price': total_price,  # Include total price in the context
#         # Add any other necessary context variables here
#     }
#     return render(request, 'shoppingcart.html', context)

def my_cart_page(request):
    # Get the raw JSON data from the request body
    # try:
    #     data = json.loads(request.body)
    #     products_info = data.POST
    # except json.JSONDecodeError:
    #     products_info = {}

    products_info = dict(request.POST)
    print(products_info)

    products = []

    total_items = 0  # Initialize total items counter
    total_price = 0  # Initialize total price accumulator

    for product_name, quantity in products_info.items():
        # Find the product in the database
        try:
            product = pt.objects.get(product_name=product_name)
        except pt.DoesNotExist:
            # Handle case when product is not found
            continue

        # Get the image name from the product
        # image_name = product_name #this is the name in the database
        # Construct the path to the product image
        # Hardcoding the absolute path to the images directory
        # image_directory = "C:/NRICARGO/my_project_rel_1/static/image"  # Use forward slashes for paths

        # Constructing the image path
        # image_path = os.path.join(image_directory, product_name + '.jpg')

        # Save the image to the product_image folder
        # You need to implement this part

        # Retrieve the price of the product
        price = product.product_price

        # Retrieve user_id from session
        user_id = request.session.get('user_id')

        # Increment total_items by the quantity of the current product
        total_items += int(quantity[0])

        # Calculate the total price of the current product and add it to total_price
        total_price += price * int(quantity[0])

        # Construct a dictionary containing product information
        product_data = {
            'user_id': user_id,
            # 'image_path': image_path,
            'name': product_name,
            'quantity': int(quantity[0]),
            'price': price * int(quantity[0]),
        }
        products.append(product_data)

        # Render the cart page with information about all products
    context = {
        'products': products,
        'total_items': total_items,  # Include total items in the context
        'total_price': total_price,  # Include total price in the context
        # Add any other necessary context variables here
    }
    return render(request, 'shoppingcart.html', context)

def save_shipping_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        user_id = request.session.get('user_id')  # Retrieve user ID from session
        # Save shipping address to the database
        # new_shipping_address = ShippingTable(shipping_address=address, user_id=user_id)
        new_shipping_address = ShippingTable()
        new_shipping_address.shipping_address= address
        new_shipping_address.user_id = user_id
        # new_shipping_address.order_id = 1
        new_shipping_address.save()

        return render(request,'orderplaced.html', {})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)