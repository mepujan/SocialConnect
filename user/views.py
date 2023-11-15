
from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, LoginForm, SignUpForm
from .models import Profile, Relationship
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q


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


# @login_required(login_url='/profile/login')
# def friend_request_received(request):
#     profile = Profile.objects.get(user=request.user)
#     qs = Relationship.objects.invitation_received(receiver=profile)
#     context = {
#         'requests': qs
#     }
#     return render(request, 'friend-request.html', context)


class FriendRequestReceivedView(ListView):
    model = Profile
    template_name = 'friends.html'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        qs = Relationship.objects.invitation_received(receiver=profile)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        context['profile'] = profile

        relation_receiver = Relationship.objects.filter(receiver=profile)

        rel_receiver = []
        for profile_ in relation_receiver:
            rel_receiver.append(profile_.receiver.user)
            print('receiver -> ', profile_.receiver.user)

        context['receiver'] = rel_receiver
        request_available = Relationship.objects.filter(
            Q(receiver=profile) & Q(status="send"))

        context['request_count'] = len(request_available)

        return context


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


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'people-list.html'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        context['profile'] = profile

        relation_receiver = Relationship.objects.filter(sender=profile)
        relation_sender = Relationship.objects.filter(receiver=profile)

        rel_sender = []
        rel_receiver = []
        for profile_ in relation_receiver:
            rel_receiver.append(profile_.receiver.user)

        for profile_ in relation_sender:
            rel_sender.append(profile_.sender.user)

        context['sender'] = rel_sender
        context['receiver'] = rel_receiver
        request_available = Relationship.objects.filter(
            Q(receiver=profile) & Q(status="send"))
        context['request_count'] = len(request_available)

        return context


@login_required(login_url='/profile/login')
def send_friend_request(request, user_id):
    sender = Profile.objects.get(user=request.user)
    receiver = Profile.objects.get(id=user_id)
    Relationship.objects.create(
        sender=sender, receiver=receiver, status='send')
    return redirect("/profile/peoples")


@login_required(login_url='/profile/login')
def remove_friend(request, user_id):
    sender = Profile.objects.get(user=request.user)
    receiver = Profile.objects.get(id=user_id)
    rel = Relationship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | (
        Q(sender=receiver) & Q(receiver=sender)))
    rel.delete()
    return redirect('/profile/peoples')


@login_required(login_url='/profile/login')
def cancel_friend_request(request, user_id):
    sender = Profile.objects.get(user=request.user)
    receiver = Profile.objects.get(id=user_id)
    rel = Relationship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | (
        Q(sender=receiver) & Q(receiver=sender)))
    rel.delete()
    return redirect('/profile/peoples')


class ViewFriendList(ListView):
    model = Profile
    template_name = 'people-list.html'

    def get_queryset(self):
        qs = Profile.objects.friends_list(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        request_available = Relationship.objects.filter(
            Q(receiver=profile) & Q(status="send"))
        context['request_count'] = len(request_available)
        return context


def accept_friend_request(request, profile_id):
    receiver = Profile.objects.get(user=request.user)
    sender = Profile.objects.get(id=profile_id)
    relationship = Relationship.objects.get(
        Q(sender=sender) & Q(receiver=receiver))
    relationship.status = 'accepted'
    relationship.save()
    return redirect('/profile/friends')
