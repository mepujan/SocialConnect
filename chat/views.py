from django.shortcuts import render, redirect
from .models import ChatMessage
from django.db.models import Q


def chat_page(request, id):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {
        'receiver_id': id
    }
    return render(request, "chat_page.html", context)


def display_all_user_messages(request):
    messages = ChatMessage.objects.filter(
        Q(sender=request.user.id) | Q(receiver=request.user.id))
    return render(request, 'messages.html', {'messages': messages})
