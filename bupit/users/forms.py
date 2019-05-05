from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model, forms as auth_forms


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


class UserSettingsForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        required=False,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        required=False,
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta(auth_forms.UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if self.cleaned_data['password1'] and self.cleaned_data['password2']:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
