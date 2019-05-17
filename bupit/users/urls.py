from django.urls import path
from . import views as user_views

urlpatterns = [
    path('<int:pk>/', user_views.UserDetailView.as_view(), name='user-detail'),
]
