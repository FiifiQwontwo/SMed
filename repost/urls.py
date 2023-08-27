from django.urls import path
from .views import RepostView

app_name = 'repost'

urlpatterns = [
    path('create/', RepostView.as_view(), name='repost_endpoint'),

]
