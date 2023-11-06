from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from posts.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    quote = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile')

    def __str__(self) -> str:
        return f'{self.user.username} profile has been created at {datetime.strptime(self.updated, "%a,%d %b, %Y %I:%M:%S %p")}.'
