from django.conf import settings
from django.db import models
from django.shortcuts import reverse


class TeacherProfile(models.Model):
    STATUS_DISABLED = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_DISABLED, 'Disabled'),
        (STATUS_ACTIVE, 'Active')
    )

    # Base
    teacher_email = models.EmailField(
        help_text="Email-address for correspondence related to your teacher profile."
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
        upload_to='teacher_photos/%Y/%m/%d',
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    #phone_number = models.CharField(max_length=50)

    def get_absolute_url(self):
        """
        Return value is used by creation views to redirect after successful
        creation of a User instance.
        """
        return reverse('teacher-profile-settings', kwargs={'pk': self.pk})

    def __str__(self):
        return u"name: %s user: %s status: %s" % (
            self.name,
            self.user.username,
            dict(self.STATUS_CHOICES)[self.status]
        )
