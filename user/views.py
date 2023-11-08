from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserUpdateForm, LoginForm, SignUpForm
from .models import Profile


def profile(request):
    profile_ = Profile.objects.get(user=request.user)
    update_form = UserUpdateForm(instance=profile_)
    return render(request, 'profile.html', {'form': update_form})


def update_profile(request):
    profile_ = Profile.objects.get(user=request.user)
    print("--> ", profile_)
    update_form = UserUpdateForm(instance=profile_)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/profile")
    return render(request, 'profile.html', {'form': update_form})


def create_profile(request):
    form = UserUpdateForm()
    if request.method == "POST":
        profile_ = Profile.objects.get(user=request.user)
        form = UserUpdateForm(request.POST, request.FILES, instance=profile_)
        if form.is_valid():
            instance = form.save(commit=False)
            print(request.user)
            instance.user = request.user
            instance.save()
            return redirect("/profile")
    return render(request, 'add-user.html', {'form': form})


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
