from .forms import UserSettingsForm
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import SettingsTabsMixin


class UserUpdateView(LoginRequiredMixin, SettingsTabsMixin, UpdateView):
    form_class = UserSettingsForm
    model = get_user_model()
    template_name = 'users/user_settings.html'
    active_settings = SettingsTabsMixin.GENERAL_SETTINGS


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    login_url = reverse_lazy('login')
    template_name = 'users/user_home.html'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(self.model, pk=self.request.user.pk)
