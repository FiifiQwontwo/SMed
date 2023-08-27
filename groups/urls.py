from django.urls import path
from .views import CreateGroupView
app_name = 'groups'

urlpatterns = [
    path('create/', CreateGroupView.as_view(), name='create_group_endpoint'),

]
