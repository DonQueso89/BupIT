from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from teachers.models import TeacherProfile
from teachers.forms import TeacherProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from utils import RequestInFormMixin, TeacherNavbarMixin, StudentNavbarMixin


class TeacherAccessControlMixin(UserPassesTestMixin):
    permission_denied_message = "Unauthorized"

    def test_func(self):
        """
        Logged in users should only be able to to CRUD for themselves.
        """
        return int(self.request.user.teacherprofile.id) == int(self.kwargs['pk'])


class TeacherProfileDetailView(LoginRequiredMixin, TeacherAccessControlMixin, DetailView):
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


class TeacherProfileUpdateView(LoginRequiredMixin, TeacherAccessControlMixin, TeacherNavbarMixin, RequestInFormMixin, SuccessMessageMixin, UpdateView):
    form_class = TeacherProfileUpdateForm
    model = TeacherProfile
    login_url = '/login/'
    template_name = 'teachers/teacher_settings.html'
    active_nav_item = TeacherNavbarMixin.NAV_ITEM_SETTINGS
    success_message = "Profile was updated successfully"

    def form_valid(self, form):
        # Also save the form of the related user
        user_form = form.user_form
        if user_form.has_changed and user_form.is_valid():
            user_form.save()
        if form.has_changed or user_form.has_changed:
            messages.success(
                self.request,
                'Successfully updated profile details'
            )
        return super().form_valid(form)


class TeacherDashboardView(LoginRequiredMixin, StudentNavbarMixin, TemplateView):
    login_url = '/login/'
    template_name = 'teachers/teacher_dashboard.html'
    active_nav_item = StudentNavbarMixin.NAV_ITEM_DASHBOARD
