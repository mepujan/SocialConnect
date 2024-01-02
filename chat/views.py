from django.shortcuts import render, redirect
from .models import ChatMessage
from django.db.models import Q


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat_page.html", context)


def display_all_user_messages(request, id):
    messages = ChatMessage.objects.filter(Q(sender=id) | Q(receiver=id))
    print('messages ->', messages)
    return render(request, 'messages.html', {'messages': messages})
