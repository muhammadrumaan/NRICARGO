from django.shortcuts import render, HttpResponse, redirect
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
        user_exist = CredentialsTable.objects.filter(username= username, password=password).exists()
        print(request.POST)

        if user_exist:
            user_id = CredentialsTable.objects.filter(username= username)[0].user_id
            request.session['user_id']=user_id
            return redirect('/pns/products')

        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'index.html', {'error_message': error_message})


def add_newuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        country = request.POST.get('country')
        password = request.POST.get('password')

        new_user = CredentialsTable()
        new_user.username = username
        new_user.email = email
        new_user.mobile = mobile
        new_user.country = country
        new_user.password = password

        new_user.save()

        return redirect('/login')

    else:
        return HttpResponse("Not received")

