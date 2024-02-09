from django.shortcuts import render, HttpResponse
from .models import CredentialsTable

# Create your views here.
def login_page(request):
    return render(request, 'index.html', {})

def newuser_page(request):
    return render(request, 'newuser.html', {})


def home_page(request):
    return render(request, 'home.html', {})

def login_verification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user_exist = UserModel.objects.filter(username= username).exists()
        #
        # if user_exist:
        #     pass
        # else:
        #     error_message = 'Invalid credentials. Please try again.'
        #     return render(request, 'index.html', {'error_message': error_message})
