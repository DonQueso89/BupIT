from django.db import models


class Student(models.Model):
    STATUS_DISABLED = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_DISABLED, 'Disabled'),
        (STATUS_ACTIVE, 'Active')
    )
    name = models.CharField(max_length=200)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_DISABLED
    )
    date_created = models.DateTimeField(auto_now_add=True)
