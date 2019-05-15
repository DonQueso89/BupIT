from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.shortcuts import reverse


class TeacherProfile(models.Model):
    STATUS_DISABLED = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_DISABLED, 'Disabled'),
        (STATUS_ACTIVE, 'Active')
    )
    
    SUBJECT_WISKUNDEA = 0
    SUBJECT_WISKUNDEB = 1
    SUBJECT_NATUURKUNDE = 2
    SUBJECT_SCHEIKUNDE = 3
    SUBJECT_CHOICES = (
        (SUBJECT_WISKUNDEA, 'Wiskunde A'),
        (SUBJECT_WISKUNDEB, 'Wiskunde B'),
        (SUBJECT_NATUURKUNDE, 'Natuurkunde'),
        (SUBJECT_SCHEIKUNDE, 'Scheikunde'),
    )

    teacher_email = models.EmailField(
        help_text="Email-address for correspondence related to your teacher profile."
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DISABLED)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to='teacher_photos/%Y/%m/%d', blank=True)
    subjects = ArrayField(models.IntegerField(choices=SUBJECT_CHOICES), blank=True, default=list)
    hourprice = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """
        Return value is used by creation views to redirect after successful
        creation of a User instance.
        """
        return reverse('teacher-profile-settings', kwargs={'pk': self.pk})

    def __str__(self):
        return u"user: %s status: %s" % (
            self.user.username,
            dict(self.STATUS_CHOICES)[self.status]
        )
