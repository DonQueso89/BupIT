from django.conf import settings
from django.db import models


class StudentProfile(models.Model):
    STATUS_DISABLED = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_DISABLED, 'Disabled'),
        (STATUS_ACTIVE, 'Active')
    )

    # Base
    name = models.CharField(max_length=200)
    email = models.EmailField(
        help_text="Email-address for correspondence related to your student profile"
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_DISABLED
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(
        upload_to='student_photos/%Y/%m/%d'
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"name: %s user: %s status: %s" % (
            self.name,
            self.user.username,
            dict(self.STATUS_CHOICES)[self.status]
        )
