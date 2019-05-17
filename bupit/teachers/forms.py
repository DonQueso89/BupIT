from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, HTML
from crispy_forms.bootstrap import Tab, TabHolder
from teachers.models import TeacherProfile
from users.forms import UserUpdateForm
from utils.crispy_building_blocks import Col, Row


class TeacherProfileUpdateForm(forms.ModelForm):
        subjects = forms.MultipleChoiceField(required=False, choices=TeacherProfile.SUBJECT_CHOICES)

        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request')
            super().__init__(*args, **kwargs)
            self.fields['subjects'].label = 'Vakken'
            self.fields['teacher_email'].label = 'Leraar email'
            self.fields['profile_picture'].label = 'Profielfoto'
            self.fields['hourprice'].label = 'Uurprijs'

            self.helper = FormHelper()
            self.helper.layout = Layout(
                TabHolder(
                    Tab(
                        'Algemeen',
                        HTML('{% load crispy_forms_tags %}{% crispy form.user_form %}')
                    ),
                    Tab(
                        'LeraarProfiel',
                        Row(
                            Col('teacher_email'),
                            Col('hourprice'),
                        ),
                        Row(
                            Col('subjects'),
                        ),
                        Row(
                            Col(
                                HTML("""{% if form.profile_picture.value %}<img class="img-responsive img-fluid rounded" src="{{ MEDIA_URL }}{{ form.profile_picture.value }}">{% endif %}""", ),
                                css_class='col-sm-1'
                            ),
                            Col('profile_picture'),
                        ),
                    ),
                    Tab('Beschikbaarheid'),
                    Tab('Preview'),
                )
            )
            self.helper.add_input(Submit("submit", "Update profiel"))

            if self.request.method == 'GET':
                self.user_form = UserUpdateForm(instance=self.request.user)
            else:
                self.user_form = UserUpdateForm(
                    data=self.request.POST,
                    instance=self.request.user,
                    initial={
                        field: getattr(self.request.user, field) for field in UserUpdateForm.Meta.fields
                    }
                )

        def clean_subjects(self):
            value = self.cleaned_data.get('subjects')
            if not value:
                return []
            return [int(x) for x in value]

        def clean(self, *args, **kwargs):
            if not self.user_form.is_valid():
                raise forms.ValidationError("Please correct the errors below")
            cleaned_data = super().clean(*args, **kwargs)
            return cleaned_data

        class Meta(object):
            model = TeacherProfile
            fields = (
                'teacher_email',
                'profile_picture',
                'subjects',
                'hourprice',
            )
