from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/', views.success, name='success'),
    path('attractions/', views.attractions, name='attractions'),
    path('conservation/', views.conservation, name='conservation'),
    path('booking/', views.booking, name='booking'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
