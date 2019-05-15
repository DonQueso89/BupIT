from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from teachers.models import TeacherProfile
from teachers.forms import TeacherProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import RequestInFormMixin, TeacherNavbarMixin, StudentNavbarMixin


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


class TeacherProfileUpdateView(LoginRequiredMixin, TeacherNavbarMixin, RequestInFormMixin, UpdateView):
    form_class = TeacherProfileUpdateForm
    model = TeacherProfile
    login_url = '/login/'
    template_name = 'teachers/teacher_settings.html'
    active_nav_item = TeacherNavbarMixin.NAV_ITEM_SETTINGS


class TeacherDashboardView(LoginRequiredMixin, StudentNavbarMixin, TemplateView):
    login_url = '/login/'
    template_name = 'teachers/teacher_dashboard.html'
    active_nav_item = StudentNavbarMixin.NAV_ITEM_DASHBOARD
