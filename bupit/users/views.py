from .forms import RegisterUserForm, UserSettingsForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import SettingsTabsMixin


class UserCreateView(CreateView):
    form_class = RegisterUserForm
    model = get_user_model()
    success_url = '/login/'


class UserUpdateView(LoginRequiredMixin, SettingsTabsMixin, UpdateView):
    form_class = UserSettingsForm
    model = get_user_model()
    template_name = 'users/user_settings.html'
    active_settings = SettingsTabsMixin.GENERAL_SETTINGS


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    login_url = '/login/'
    template_name = 'users/user_home.html'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(self.model, pk=self.request.user.pk)
