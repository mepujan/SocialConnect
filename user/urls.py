from django.urls import path
from .views import profile, create_profile, login_user, signup


app_name = 'profiles'

urlpatterns = [
    path("", profile, name='profile'),
    path("add-profile", create_profile, name="create_profile"),
    path("login", login_user, name='login'),
    path('signup', signup, name='signup')
]
