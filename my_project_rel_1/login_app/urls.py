# from django.urls import path
# from .views import login_page, newuser_page, home_page, login_verification, add_newuser
#
# urlpatterns = [
#     path('',login_page),
#     path('newuser/', newuser_page),
#     path('home/', home_page),
#     path('post/', login_verification),
#     path('add_newuser/',add_newuser)
#
# ]
# login_app/urls.py

from django.urls import path
from .views import login_page, newuser_page, home_page, login_verification, add_newuser

app_name = 'login_app'  # Add this line to define the app's namespace

urlpatterns = [
    path('', login_page, name='login_page'),
    path('newuser/', newuser_page, name='newuser_page'),
    path('home/', home_page, name='home_page'),
    path('post/', login_verification, name='login_verification'),
    path('add_newuser/', add_newuser, name='add_newuser'),
]
