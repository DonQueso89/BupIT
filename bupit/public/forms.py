from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from students.models import StudentProfile
from teachers.models import TeacherProfile


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('login')
        self.helper.add_input(Submit("submit", "Submit"))


class UserRegistrationForm(UserCreationForm):
    prefix = 'user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm._meta.fields + (
            'first_name',
            'last_name',
        )


class StudentRegistrationForm(forms.ModelForm):
    prefix = 'sp'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Aanmelden"))
        self.helper.form_tag = False

    class Meta(object):
        model = StudentProfile
        fields = (
            'profile_picture',
            'student_email',
        )


class TeacherRegistrationForm(forms.ModelForm):
    prefix = 'tp'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Aanmelden"))
        self.helper.form_tag = False

    class Meta(object):
        model = TeacherProfile
        fields = (
            'profile_picture',
            'teacher_email',
        )
