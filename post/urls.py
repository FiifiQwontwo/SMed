from django.urls import path
from .views import CreatePostView, UpdatePostView, DeletePostView

app_name = 'post'

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post_endpoint'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update_post_endpoint'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_post_endpoint'),
    # path('create/', CreatePostView.as_view(), name='asd'),
]
