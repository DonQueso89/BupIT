from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import forms, get_user_model


class RegisterUserForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'user-create'
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        fields = ('username',)
        model = get_user_model()
