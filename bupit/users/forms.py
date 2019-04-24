from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import forms, get_user_model


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


class RegisterUserForm(forms.UserCreationForm):
    """
    Looks for user_form.html by default to use as template
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'user-create'
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta(forms.UserCreationForm.Meta):
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields + ('my_fields',)


class UserSettingsForm(forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta(forms.UserChangeForm):
        model = get_user_model()
        fields = ('username',)
