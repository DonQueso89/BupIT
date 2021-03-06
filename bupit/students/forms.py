from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from students.models import StudentProfile
from utils import RequestInFormMixin


class StudentProfileForm(forms.ModelForm, RequestInFormMixin):
        user = forms.IntegerField(widget=forms.HiddenInput())

        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request')
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.add_input(Submit("submit", "Submit"))

        class Meta(object):
            model = StudentProfile
            fields = (
                'student_email',
                'profile_picture',
                'user',
            )

        def clean(self):
            """
            We need to enforce that a user only creates BUPs for himself.
            This may not be the case if somebody messes with the  hidden POST data.
            """
            cleaned_data = super().clean()
            if int(cleaned_data.get('user', -1)) != int(self.request.user.pk):
                raise forms.ValidationError("Please dont mess with hidden POST data.")
            return cleaned_data
