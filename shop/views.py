# shop/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from . import views

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

# shop/views.py
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

# shop/views.py


def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

