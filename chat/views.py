from django.shortcuts import render, redirect
from .models import ChatMessage
from django.db.models import Q
from user.models import Profile


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat_page.html", context)


def display_all_user_messages(request, id):
    messages = ChatMessage.objects.filter(Q(sender=id) | Q(receiver=id))
    return render(request, 'messages.html', {'messages': messages})
