from django.urls import path
from .views import profile, create_profile

app_name = 'profiles'

urlpatterns = [
    path("", profile, name='profile'),
    path("add-profile", create_profile, name="create_profile")
]
