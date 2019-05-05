from django.shortcuts import reverse


class RequestInFormMixin(object):
    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super().get_form_kwargs(*args, **kwargs)
            kwargs['request'] = self.request
            return kwargs


class SettingsTabsMixin(object):
    """
    Adds a list of applicable settings tabs to the template context
    """
    GENERAL_SETTINGS = 0
    STUDENT_SETTINGS = 1
    TEACHER_SETTINGS = 2

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        settings_tabs = [
                {
                    "name": "General settings",
                    "active": self.active_settings == self.GENERAL_SETTINGS,
                    "url": reverse("user-settings", kwargs={"pk": self.request.user.pk})
                }
        ]
        if self.request.user.is_teacher():
            settings_tabs.append(
                {
                    "name": "Teacher settings",
                    "active": self.active_settings == self.TEACHER_SETTINGS,
                    "url": reverse("teacher-profile-settings", kwargs={"pk": self.request.user.teacherprofile.pk})
                }
            )
        if self.request.user.is_student():
            settings_tabs.append(
                {
                    "name": "Student settings",
                    "active": self.active_settings == self.STUDENT_SETTINGS,
                    "url": reverse("student-profile-settings", kwargs={"pk": self.request.user.studentprofile.pk})
                }
            )
        ctx['settings_tabs'] = settings_tabs
        return ctx
