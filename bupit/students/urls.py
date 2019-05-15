from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.StudentDashboardView.as_view(), name='student-dashboard'),
    path('<int:pk>/', views.StudentProfileDetailView.as_view(), name='student-profile-detail'),
    path('update/<int:pk>/', views.StudentProfileUpdateView.as_view(), name='student-profile-settings'),
]
