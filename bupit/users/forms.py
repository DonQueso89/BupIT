from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib.auth import get_user_model, forms as auth_forms
from utils.crispy_building_blocks import Col, Row



"""
The following forms are compatible with any subclass of AbstractBaseUser:

AuthenticationForm: Uses the username field specified by USERNAME_FIELD.
SetPasswordForm
PasswordChangeForm
AdminPasswordChangeForm
The following forms make assumptions about the user model and can be used as-is if those assumptions are met:

PasswordResetForm: Assumes that the user model has a field that stores the user’s email address with the name returned by get_email_field_name() (email by default) that can be used to identify the user and a boolean field named is_active to prevent password resets for inactive users.
Finally, the following forms are tied to User and need to be rewritten or extended to work with a custom user model:

UserCreationForm
UserChangeForm
"""


class UserUpdateForm(auth_forms.UserChangeForm):
    """
    For use in either Teacher or Student settings forms.
    """
    prefix = 'user'
    helper = FormHelper()
    helper.form_tag = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Field translation
        self.fields['first_name'].label = 'Voornaam'
        self.fields['last_name'].label = 'Achternaam'
        self.fields['username'].label = 'Gebruikersnaam'
        self.fields['phonenumber'].label = 'Telefoonnummer'
        self.fields['email'].label = 'Email'

        self.helper.layout = Layout(
            Row(Col('username'), Col('first_name'), Col('last_name')),
            Row(Col('phonenumber'), Col('email')),
        )

    class Meta(auth_forms.UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phonenumber',
        )
