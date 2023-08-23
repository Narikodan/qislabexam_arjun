from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import EventForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request,'index.html')



def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'coordinator':
                return redirect('admin_section')  
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')

def dashboard(request):
    return render(request,'index.html')

def admin_section(request):
    return render(request,'admin_section.html')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)  # Print form errors to the console for debugging
        return redirect('admin_section')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})
