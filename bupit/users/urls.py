from django.urls import path
from . import views as user_views

urlpatterns = [
    path('create/', user_views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', user_views.UserDetailView.as_view(), name='user-detail'),
    path('update/<int:pk>/', user_views.UserUpdateView.as_view(), name='user-settings'),
]
