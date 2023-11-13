from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from datetime import datetime
from abstract.abstract import BaseModel
from django.db.models import Q

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class ProfileManager(models.Manager):
    def get_all_profiles(self, me):
        qs = Profile.objects.exclude(user=me).all()
        return qs

    def get_all_profiles_to_add(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(
            Q(sender=profile) | Q(receiver=profile))

        accepted_profile = []
        for relation in qs:
            if relation.status == 'accepted':
                accepted_profile.append(relation.sender)
                accepted_profile.append(relation.receiver)

        available_profile = [
            profile for profile in profiles if profile not in accepted_profile]

        return available_profile


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=100)
    bio = models.TextField(max_length=200, default="no bio")
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    profile_pic = models.ImageField(upload_to='profile', default='avatar.png', validators=[
                                    FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    objects = ProfileManager()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def email(self):
        return self.user.email

    def post_count(self):
        return self.posts.count()

    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return f"{self.user.username} has created profile on {datetime.strftime(self.updated, '%a,%d %b, %Y %I:%M:%S %p')}"


class RelationshipManager(models.Manager):
    def invitation_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status="send")
        return qs


class Relationship(BaseModel):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    objects = RelationshipManager()

    def __str__(self) -> str:
        return f"{self.sender.user.username} send friend request to {self.receiver.user.username}"
