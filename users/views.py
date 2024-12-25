from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def root_redirect(request):
    """Redirect '/' based on login status and role."""
    if request.user.is_authenticated:
        if request.user.is_admin():
            return redirect('dashboard')  # Admin goes to dashboard
        return redirect('machine_list')  # Employee goes to machines
    return redirect('login')  # Redirect to login if not authenticated

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_admin():
                    return HttpResponseRedirect(reverse('dashboard')) 
                return HttpResponseRedirect(reverse('machine_list')) 
            else:
                messages.error(request, "Account is deactivated.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    if request.user.is_admin():  # Check if the logged-in user is an admin
        return render(request, 'users/dashboard.html')  # Render the admin dashboard
    else:
        return redirect('machine_list') 