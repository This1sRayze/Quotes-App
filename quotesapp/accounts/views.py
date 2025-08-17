from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes:root')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form, 'hide_auth_buttons': True})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quotes:root')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'hide_auth_buttons': True})

def logout_view(request):
    # allow GET or POST logout for convenience; then redirect to home
    logout(request)
    return redirect('quotes:root')
