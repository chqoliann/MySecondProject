from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


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