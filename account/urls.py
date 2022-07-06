from django.urls import path
from . import views

urlpatterns = [
    path('', views.tambah_data),
    path('home', views.tambah_data),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('history', views.history,name='history'),
    path('result', views.result,name='result'),
    path('preview', views.preview,name='preview'),
    # path('coba_fungsi', views.coba_fungsi)
]