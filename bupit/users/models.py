from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model that behaves exactly the same as the builtin User but has to be
    created at project start if we expect to customise this down the road.
    """
    pass
