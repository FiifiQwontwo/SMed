from django.urls import path
from .views import FollowUserView, UnfollowUserView

app_name = 'followers'

urlpatterns = [
    path('follow/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
