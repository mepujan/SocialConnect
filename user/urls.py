from django.urls import path
from .views import (profile, create_profile, login_user, signup, logout_user,
                    ProfileDetailView, search_user,
                    profiles_to_add_friend, ProfileListView,
                    send_friend_request, remove_friend, cancel_friend_request,
                    ViewFriendList, FriendRequestReceivedView, accept_friend_request)


app_name = 'profiles'

urlpatterns = [
    path("", profile, name='profile'),
    path("add-profile", create_profile, name="create_profile"),
    path("login", login_user, name='login'),
    path('signup', signup, name='signup'),
    path("logout", logout_user, name='logout'),
    path("<int:pk>/profile", ProfileDetailView.as_view(), name="profile-detail"),
    path('search', search_user, name='search-user'),
    path('add-friend', profiles_to_add_friend, name='add-friend'),
    path('peoples', ProfileListView.as_view(), name='peoples'),
    path('add-friend/<int:user_id>', send_friend_request, name='add-friend'),
    path('remove-friend/<int:user_id>', remove_friend, name='remove-friend'),
    path('cancel-friend/<int:user_id>',
         cancel_friend_request, name='cancel-request'),
    path('friends', ViewFriendList.as_view(), name='friends'),
    path('requests', FriendRequestReceivedView.as_view(), name='friend-request'),
    path('accept_request/<int:profile_id>',
         accept_friend_request, name='accept-friend')

]
