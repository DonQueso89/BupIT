from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/success/', views.registration_success, name='registration-success'),
    path('register/choice/', views.registration_choice, name='registration-choice'),
    path('register/<register_as>/', views.register, name='register'),
]
