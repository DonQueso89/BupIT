from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from students.models import StudentProfile
from students.forms import StudentProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import RequestInFormMixin, SettingsTabsMixin, StudentNavbarMixin, TeacherNavbarMixin


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


class StudentProfileUpdateView(LoginRequiredMixin, StudentNavbarMixin, RequestInFormMixin, UpdateView):
    form_class = StudentProfileForm
    model = StudentProfile
    login_url = '/login/'
    template_name = 'students/student_settings.html'
    active_nav_item = StudentNavbarMixin.NAV_ITEM_SETTINGS


class StudentDashboardView(LoginRequiredMixin, TeacherNavbarMixin, TemplateView):
    login_url = '/login/'
    template_name = 'students/student_dashboard.html'
    active_nav_item = TeacherNavbarMixin.NAV_ITEM_DASHBOARD
