from django.db import models
from django.contrib.auth.models import User
from abstract.abstract import BaseModel
from user.models import Profile


class ChatMessage(BaseModel):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='msg_sender')
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='msg_receiver')
    message = models.TextField()

    def __str__(self):
        return f"{self.sender.user.username} send message to {self.receiver.user.username}"
