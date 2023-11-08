from django.shortcuts import render, redirect
from .forms import UserUpdateForm
from .models import Profile


def profile(request):
    profile_ = Profile.objects.get(user=request.user)
    update_form = UserUpdateForm(instance=profile_)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/profile")
    return render(request, 'profile.html', {'form': update_form})


def create_profile(request):
    form = UserUpdateForm()
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/profile")
    return render(request, 'add-user.html', {'form': form})
