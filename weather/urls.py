from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('history/', views.history, name='history'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
