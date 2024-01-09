from django.urls import path
from .views import chat_page, display_all_user_messages

app_name = 'chat'

urlpatterns = [
    path('message/<int:id>/', chat_page, name='message'),
    path('messages/', display_all_user_messages, name='messages')
]
