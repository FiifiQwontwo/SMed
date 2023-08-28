from django.urls import path
from .views import MembershipListView, MembershipView, MembershipDetailView, UpdateMembersView, DeleteMembershipView

app_name = 'membership'

urlpatterns = [
    path('memberships/', MembershipListView.as_view(), name='membership-list'),
    path('memberships/create/', MembershipView.as_view(), name='membership-create'),
    path('memberships/<int:membership_id>/', MembershipDetailView.as_view(), name='membership-detail'),
    path('memberships/<int:membership_id>/update/', UpdateMembersView.as_view(), name='membership-update'),
    path('memberships/<int:membership_id>/delete/', DeleteMembershipView.as_view(), name='membership-delete'),
]
