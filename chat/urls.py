from django.urls import path
from .views import chatPage

app_name = 'chat'

urlpatterns = [
    path('message/<int:id>', chatPage, name='message')
]
