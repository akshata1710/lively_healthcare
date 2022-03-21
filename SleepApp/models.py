

from datetime import time
from django.db import models


# Create your models here.
class Slee(models.Model):
    hours = models.IntegerField()

    DAYS_OF_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    days = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
