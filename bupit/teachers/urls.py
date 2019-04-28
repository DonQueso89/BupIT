from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.TeacherProfileCreateView.as_view(), name='teacher-profile-create'),
    path('<int:pk>/', views.TeacherProfileDetailView.as_view(), name='teacher-profile-detail'),
    path('update/<int:pk>/', views.TeacherProfileUpdateView.as_view(), name='teacher-profile-settings'),
]
