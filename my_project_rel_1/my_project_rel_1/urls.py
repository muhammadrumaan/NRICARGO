"""
my_project_rel_1/urls
"""
from django.contrib import admin
from django.urls import path, include
import cartapp.urls
import pns.urls
import homeapp.urls
import login_app.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homeapp.urls)),
    path('cart/', include(cartapp.urls)),
    path('login/', include(login_app.urls)),
    path('pns/', include(pns.urls)),
]

# http://127.0.0.1:8000/cartapp/