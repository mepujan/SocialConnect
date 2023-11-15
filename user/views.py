from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, LoginForm, SignUpForm
from .models import Profile, Relationship
from django.views.generic import DetailView, ListView
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
def search_user(request):
    users = User.objects.get(username=request.POST.get('username'))
    profile = Profile.objects.filter(user=users)
    profile_ = Profile.objects.get(user=request.user)
    context = {
        'profiles': profile,
        'profile': profile_
    }
    return render(request, 'people-list.html', context)


@login_required(login_url='/profile/login')
def friend_request_received(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitation_received(receiver=profile)
    context = {
        'requests': qs
    }
    return render(request, 'friend-request.html', context)


@login_required(login_url='/profile/login')
def profiles_to_add_friend(request):
    profiles = Profile.objects.get_all_profiles_to_add(request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'to-add-friend.html', context)


@login_required(login_url='/profile/login')
def get_all_user(request):
    profile_ = Profile.objects.get(user=request.user)
    profiles = Profile.objects.get_all_profiles(request.user)
    context = {
        'profiles': profiles,
        'profile': profile_
    }
    return render(request, 'people-list.html', context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'people-list.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        context['profile'] = profile

        relation_receiver = Relationship.objects.filter(sender=profile)
        relation_sender = Relationship.objects.filter(receiver=profile)
        print("rel-sender ->", relation_sender)
        print("rel-receiver ->", relation_receiver)

        rel_sender = []
        rel_receiver = []
        for profile_ in relation_receiver:
            rel_receiver.append(profile_.receiver.user)

        for profile_ in relation_sender:
            rel_sender.append(profile_.sender.user)

        context['sender'] = rel_sender
        context['receiver'] = rel_receiver

        return context


def send_friend_request(request, user_id):
    sender = Profile.objects.get(user=request.user)
    receiver = Profile.objects.get(id=user_id)
    Relationship.objects.create(
        sender=sender, receiver=receiver, status='send')
    return redirect("/profile/peoples")
