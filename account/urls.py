from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('home', views.welcome,name='welcome'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('history', views.history,name='history'),
]