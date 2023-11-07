from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from datetime import datetime
from abstract.abstract import BaseModel

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    quote = models.CharField(max_length=200)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    profile_pic = models.ImageField(upload_to='profile', default='avatar.png', validators=[
                                    FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return f"{self.user.username} has created profile on {datetime.strftime(self.updated, '%a,%d %b, %Y %I:%M:%S %p')}"


class Relationship(BaseModel):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.sender.user.username} send friend request to {self.receiver.user.username}"
