from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from teachers.models import TeacherProfile
from teachers.forms import TeacherProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import RequestInFormMixin, SettingsTabsMixin


class TeacherProfileCreateView(LoginRequiredMixin, SettingsTabsMixin, RequestInFormMixin, CreateView):
    form_class = TeacherProfileForm
    model = TeacherProfile
    login_url = '/login/'
    template_name = 'teachers/teacher_settings.html'
    active_settings = SettingsTabsMixin.TEACHER_SETTINGS

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Users can only create BUPs for themselves
        ctx['form'].fields['user'].initial = self.request.user.pk
        ctx['form'].fields['email'].initial = self.request.user.email
        return ctx


class TeacherProfileUpdateView(LoginRequiredMixin, SettingsTabsMixin, RequestInFormMixin, UpdateView):
    form_class = TeacherProfileForm
    model = TeacherProfile
    login_url = '/login/'
    template_name = 'teachers/teacher_settings.html'
    active_settings = SettingsTabsMixin.TEACHER_SETTINGS

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class TeacherProfileDetailView(LoginRequiredMixin, DetailView):
    model = TeacherProfile
    login_url = '/login/'
    template_name = 'teachers/teacher_detail.html'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(
            self.model,
            pk=self.request.user.teacherprofile.pk
        )
