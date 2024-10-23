# users/urls.py
from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
