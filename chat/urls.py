from django.urls import path
from .views import chatPage, display_all_user_messages

app_name = 'chat'

urlpatterns = [
    path('message/<int:id>', chatPage, name='message'),
    path('messages/<int:id>/', display_all_user_messages, name='messages')
]
