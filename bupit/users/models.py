from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    """
    Model that behaves exactly the same as the builtin User but has to be
    created at project start if we expect to customise this down the road.

    https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user
    """
    def get_absolute_url(self):
        """
        Return value is used by creation views to redirect after successful
        creation of a User instance.
        """
        return reverse('user-detail', kwargs={'pk': self.pk})
