from django.shortcuts import reverse


class RequestInFormMixin(object):
    def get_form_kwargs(self, *args, **kwargs):
            kwargs = super().get_form_kwargs(*args, **kwargs)
            kwargs['request'] = self.request
            return kwargs


class TeacherNavbarMixin(object):
    NAV_ITEM_SETTINGS = 0
    NAV_ITEM_DASHBOARD = 1
    NAV_ITEM_HELP_PAGE = 2

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['nav_items'] = [
            {'name': 'Vind leerlingen', 'active': self.active_nav_item == self.NAV_ITEM_DASHBOARD, 'url': reverse('student-dashboard')},
            {'name': 'Profiel', 'active': self.active_nav_item == self.NAV_ITEM_SETTINGS, 'url': reverse('teacher-profile-settings', kwargs={'pk': self.request.user.teacherprofile.pk})},
            {'name': 'Help', 'active': self.active_nav_item == self.NAV_ITEM_HELP_PAGE, 'url': reverse('student-dashboard')},
        ]
        return ctx


class StudentNavbarMixin(object):
    NAV_ITEM_SETTINGS = 0
    NAV_ITEM_DASHBOARD = 1
    NAV_ITEM_HELP_PAGE = 2

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['nav_items'] = [
            {'name': 'Vind leraren', 'active': self.active_nav_item == self.NAV_ITEM_DASHBOARD, 'url': reverse('teacher-dashboard')},
            {'name': 'Profiel', 'active': self.active_nav_item == self.NAV_ITEM_SETTINGS, 'url': reverse('student-profile-settings', kwargs={'pk': self.request.user.studentprofile.pk})},
            {'name': 'Help', 'active': self.active_nav_item == self.NAV_ITEM_HELP_PAGE, 'url': reverse('teacher-dashboard')},
        ]
        return ctx
