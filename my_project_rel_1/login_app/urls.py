from django.urls import path
from .views import login_page, newuser_page, home_page, login_verification

urlpatterns = [
    path('',login_page),
    path('newuser/', newuser_page),
    path('home/', home_page),
    path('post/',login_verification)

]