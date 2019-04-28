from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.StudentProfileCreateView.as_view(), name='student-profile-create'),
    path('<int:pk>/', views.StudentProfileDetailView.as_view(), name='student-profile-detail'),
    path('update/<int:pk>/', views.StudentProfileUpdateView.as_view(), name='student-profile-settings'),
]
