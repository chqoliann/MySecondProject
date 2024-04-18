from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                form.add_error('password2', 'password dont mach')
                return render(request, 'signup.html', {'form':form})
            else:
                form.save()
                return redirect('index')
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = "Invalid username or password."
                return render(request, 'index.html', {'form': form, 'error_message':error_message})

    else:
        form = UserLoginForm()
        return render(request, 'signin.html', {"form":form})