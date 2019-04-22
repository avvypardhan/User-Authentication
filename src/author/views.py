from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, UpdateProfileForm

def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Successfully Loged In..!'))
            return redirect('home')
        else:
            messages.success(request, ('Error...Log in failed!!'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out..!'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Completed..!'))
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Profile Updated..!'))
            return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user)
    context = {'form':form}
    return render(request, 'update_profile.html', context)

def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Password changed..!'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request, 'update_password.html', context)

