from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserManagementAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user-management/', UserManagementAPIView.as_view(), name='user-management'),
]
