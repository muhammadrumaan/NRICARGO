""""
homeapp/urls.py
"""
from django.urls import path
from .views import my_index_page

urlpatterns = [
    path('', my_index_page),
]
