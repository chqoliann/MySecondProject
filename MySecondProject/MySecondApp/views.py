from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
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
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'not account with this data')

    else:
        form = UserLoginForm()
    return render(request, 'signin.html', {'form':form})
