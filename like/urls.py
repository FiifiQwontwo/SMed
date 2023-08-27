from django.urls import path
from .views import *

app_name = 'like'

urlpatterns = [


    path('like/<int:post_id>/', LikeView.as_view(), name='likes_endpoint'),
    path('unlike/<int:post_id>/', UnlikeView.as_view(), name='unlike_endpoint'),


]
