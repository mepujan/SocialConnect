from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from posts.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    quote = models.CharField(max_length=200)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    profile_pic = models.ImageField(upload_to='profile', default='avatar.png')

    def __str__(self) -> str:
        return f"{self.user.username} has created profile on {datetime.strftime(self.updated, '%a,%d %b, %Y %I:%M:%S %p')}"
