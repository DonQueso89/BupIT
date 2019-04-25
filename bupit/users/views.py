from .forms import RegisterUserForm, UserSettingsForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model, forms as auth_forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(CreateView):
    form_class = RegisterUserForm
    model = get_user_model()
    success_url = '/login/'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserSettingsForm
    model = get_user_model()
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active_content'] = 'users/user_settings.html'
        return ctx


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    login_url = '/login/'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(self.model, pk=self.request.user.pk)
