from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.LeadListCreateView.as_view(), name='lead-list'),
    path('leads/change/<int:pk>', views.LeadRetrieveUpdateDestroy.as_view(), name='lead-list-change'),
    path('users/', views.UserListView.as_view(), name='user-list'),
]

