from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from students.models import StudentProfile
from students.forms import StudentProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import RequestInFormMixin, SettingsTabsMixin


class StudentProfileCreateView(LoginRequiredMixin, SettingsTabsMixin, RequestInFormMixin, CreateView):
    form_class = StudentProfileForm
    model = StudentProfile
    login_url = '/login/'
    template_name = 'students/student_settings.html'
    active_settings = SettingsTabsMixin.STUDENT_SETTINGS

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Users can only create BUPs for themselves
        ctx['form'].fields['user'].initial = self.request.user.pk
        ctx['form'].fields['email'].initial = self.request.user.email
        return ctx


class StudentProfileUpdateView(LoginRequiredMixin, SettingsTabsMixin, RequestInFormMixin, UpdateView):
    form_class = StudentProfileForm
    model = StudentProfile
    login_url = '/login/'
    template_name = 'students/student_settings.html'
    active_settings = SettingsTabsMixin.STUDENT_SETTINGS

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class StudentProfileDetailView(LoginRequiredMixin, DetailView):
    model = StudentProfile
    login_url = '/login/'
    template_name = 'students/student_detail.html'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(
            self.model,
            pk=self.request.user.studentprofile.pk
        )
