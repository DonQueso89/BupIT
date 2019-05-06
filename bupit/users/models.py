from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


def validate_phonenumber(value):
    if not value.isdigit():
        raise ValidationError(
            _("%(value)s is geen valide telefoonnummer"),
            params={'value': value}
        )


class User(AbstractUser):
    """
    Model that behaves exactly the same as the builtin User but has to be
    created at project start if we expect to customise this down the road.

    https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user
    """
    phonenumber = models.CharField(
        max_length=100,
        validators=[validate_phonenumber],
        help_text="Mag alleen getallen bevatten"
    )
    agreed_to_terms_and_conditions = models.BooleanField()

    def get_absolute_url(self):
        """
        Return value is used by creation views to redirect after successful
        creation of a User instance.
        """
        return reverse('user-detail', kwargs={'pk': self.pk})

    def is_student(self):
        return hasattr(self, 'studentprofile')

    def is_teacher(self):
        return hasattr(self, 'teacherprofile')
