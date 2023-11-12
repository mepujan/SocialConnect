from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, LoginForm, SignUpForm
from .models import Profile
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


@login_required(login_url='/profile/login')
def profile(request):
    profile_ = Profile.objects.get(user=request.user)
    update_form = UserUpdateForm(instance=profile_)
    return render(request, 'profile.html', {'form': update_form, 'profile': profile_})


@login_required(login_url='/profile/login')
def create_profile(request):
    form = UserUpdateForm()
    profile_ = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=profile_)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/profile")
    return render(request, 'add-user.html', {'form': form, 'profile': profile_})


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
    return render(request, 'login.html', {'form': form})


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profile/login")
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/profile/login')
def logout_user(request):
    logout(request)
    return redirect("/profile/login")


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    pk_url_kwarg = 'pk'
    template_name = 'profile.html'


@login_required(login_url='/profile/login')
def get_all_user(request):
    profile_ = Profile.objects.get(user=request.user)
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles,
        'profile': profile_
    }
    return render(request, 'people-list.html', context)


@login_required(login_url='/profile/login')
def search_user(request):
    users = User.objects.get(username=request.POST.get('username'))
    profile = Profile.objects.filter(user=users)
    profile_ = Profile.objects.get(user=request.user)
    context = {
        'profiles': profile,
        'profile': profile_
    }
    return render(request, 'people-list.html', context)
