from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.TeacherDashboardView.as_view(), name='teacher-dashboard'),
    path('<int:pk>/', views.TeacherProfileDetailView.as_view(), name='teacher-profile-detail'),
    path('update/<int:pk>/', views.TeacherProfileUpdateView.as_view(), name='teacher-profile-settings'),
]
