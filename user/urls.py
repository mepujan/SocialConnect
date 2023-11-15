from django.urls import path
from .views import (profile, create_profile, login_user, signup, logout_user,
                    ProfileDetailView, get_all_user, search_user, friend_request_received,
                    profiles_to_add_friend, ProfileListView, send_friend_request)


app_name = 'profiles'

urlpatterns = [
    path("", profile, name='profile'),
    path("add-profile", create_profile, name="create_profile"),
    path("login", login_user, name='login'),
    path('signup', signup, name='signup'),
    path("logout", logout_user, name='logout'),
    path("<int:pk>/profile", ProfileDetailView.as_view(), name="profile-detail"),
    # path('peoples', get_all_user, name='peoples'),
    path('search', search_user, name='search-user'),
    path('requests', friend_request_received, name='requests'),
    path('add-friend', profiles_to_add_friend, name='add-friend'),
    path('peoples', ProfileListView.as_view(), name='peoples'),
    path('add-friend/<int:user_id>', send_friend_request, name='add-friend')

]
