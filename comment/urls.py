from django.urls import path
from .views import *

app_name = 'comment'

urlpatterns = [

    path('newcomment/', CreateCommentView.as_view(), name='nnewcomment_endpoint'),
    path('postcomments/<int:post_id>/', CommentsForPostView.as_view(), name='post_comments_endpoint'),
    path('usercomments/<int:user_id>/', CommentsForUserView.as_view(), name='all_usercomments-endpoint'),

]
