from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, CreateUserForm, BookingForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def success(request):
    return render(request, 'success.html')

def attractions(request):
    return render(request, 'attractions.html')

def conservation(request):
    return render(request, 'conservation.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking Successful! Your booking has been successfully submitted. Thank you!')
            return redirect('crm:success')  # Redirect to success page
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("crm:home")


    context = {'registerform':form}

    return render(request, 'register.html', context=context)