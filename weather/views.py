from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import SearchHistory
from .services import get_weather_data


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'weather/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'weather/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    weather = None
    if request.method == 'POST':
        city = request.POST['city']
        weather = get_weather_data(city)
        if weather and request.user.is_authenticated:
            SearchHistory.objects.create(
                user=request.user,
                city=city,
                temperature=weather['temperature'],
                description=weather['description']
            )
    return render(request, 'weather/home.html', {'weather': weather})


@login_required
def history(request):
    searches = SearchHistory.objects.filter(user=request.user).order_by('-search_date')
    return render(request, 'weather/history.html', {'searches': searches})

