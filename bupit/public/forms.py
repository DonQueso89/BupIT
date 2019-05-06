from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout, Field
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from students.models import StudentProfile
from teachers.models import TeacherProfile


class UserAuthenticationForm(AuthenticationForm):
    im_not_a_robot = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['im_not_a_robot'].label = """
            Ik ben geen robot
        """

        self.helper = FormHelper()
        self.helper.form_action = reverse('login')
        self.helper.add_input(Submit("submit", "Submit"))


class UserRegistrationForm(UserCreationForm):
    prefix = 'user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Field translation
        self.fields['first_name'].label = 'Voornaam'
        self.fields['last_name'].label = 'Achternaam'
        self.fields['username'].label = 'Gebruikersnaam'
        self.fields['phonenumber'].label = 'Telefoonnummer'
        self.fields['password1'].label = 'Wachtwoord'
        self.fields['password2'].label = 'Bevestig wachtwoord'
        self.fields['email'].label = 'Email'
        self.fields['agreed_to_terms_and_conditions'].label = """
            Ik ga akkoord met de gebruikersvoorwaarden en de privacyvoorwaarden
        """

        # Reorganize rendering behavior
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('username', wrapper_class='col'),
                css_class='row'
            ),
            Div(
                Field('first_name', wrapper_class='col'),
                Field('last_name', wrapper_class='col'),
                css_class='row'
            ),
            Div(
                Field('phonenumber', wrapper_class='col'),
                Field('email', wrapper_class='col'),
                css_class='row'
            ),
            Div(
                Field('password1', wrapper_class='col'),
                Field('password2', wrapper_class='col'),
                css_class='row'
            ),
            Div(
                Field('agreed_to_terms_and_conditions', wrapper_class='col px-5'),
                css_class='row'
            ),
        )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm._meta.fields + (
            'first_name',
            'last_name',
            'phonenumber',
            'agreed_to_terms_and_conditions',
            'email',
        )


class StudentRegistrationForm(forms.ModelForm):
    prefix = 'sp'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Aanmelden"))
        self.helper.form_tag = False
        self.fields['profile_picture'].label = 'Profielfoto'

    class Meta(object):
        model = StudentProfile
        fields = (
            'profile_picture',
        )


class TeacherRegistrationForm(forms.ModelForm):
    prefix = 'tp'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Aanmelden"))
        self.helper.form_tag = False
        self.fields['profile_picture'].label = 'Profielfoto'

    class Meta(object):
        model = TeacherProfile
        fields = (
            'profile_picture',
        )
