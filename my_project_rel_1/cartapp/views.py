
"""
cartapp/views.py
"""

from django.shortcuts import render,HttpResponse,redirect
# from .models import Order, OrderItem

# Create your views here.

def my_cart_page(request):
    return render(request,'shoppingcart.html',{})
#
# def place_order(request):
#     # Handle form submission to place an order
#     if request.method == 'POST':
#         # Process the form data and create order objects
#         # Save order details in the database
#         # Redirect to the shopping cart page
#         return redirect('shopping_cart')
#     else:
#         # Render the form to place an order
#         return render(request, 'place_order.html')

# def shopping_cart(request):
#     # Retrieve orders from the database
#     orders = Order.objects.all()
#     # Pass orders to the template for rendering
#     return render(request, 'shoppingcart.html', {'orders': orders})
