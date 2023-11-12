from django.urls import path
from .views import profile, create_profile, login_user, signup, logout_user, ProfileDetailView, get_all_user, search_user


app_name = 'profiles'

urlpatterns = [
    path("", profile, name='profile'),
    path("add-profile", create_profile, name="create_profile"),
    path("login", login_user, name='login'),
    path('signup', signup, name='signup'),
    path("logout", logout_user, name='logout'),
    path("<int:pk>/profile", ProfileDetailView.as_view(), name="profile-detail"),
    path('peoples', get_all_user, name='peoples'),
    path('search', search_user, name='search-user')

]
