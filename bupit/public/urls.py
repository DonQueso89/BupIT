from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/<register_as>/', views.register, name='register'),
]
