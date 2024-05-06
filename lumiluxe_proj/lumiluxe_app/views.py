from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Perfume, Brand, UserProfile
from django.db.models import Q
from .forms import FeedbackForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    all_perfumes = Perfume.objects.all()
    query = request.GET.get('q')
    if query:
        all_perfumes = all_perfumes.filter(Q(perfume_name__icontains=query))
    brandes = Brand.objects.all()
    return render(request, 'index.html', {'all_perfumes': all_perfumes, 'brandes':brandes})


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
        return render(request, 'signin.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/')


def perfume_details(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    return render(request, 'perfume_details.html', {'perfume': perfume})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.date_sent = timezone.now()
            feedback.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    liked_perfumes = user_profile.liked_perfumes.all()
    return render(request, 'user_profile.html', {'user_profile': user_profile, 'liked_perfumes':liked_perfumes})


def like_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    user_profile = request.user.userprofile
    user_profile.liked_perfumes.add(perfume)
    perfume.likes += 1
    perfume.save()
    return redirect('/')