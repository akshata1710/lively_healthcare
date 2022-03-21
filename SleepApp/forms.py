
from django import forms
from matplotlib import widgets
from .models import Slee



DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class SleeForm(forms.Form):
    day = forms.CharField(
        label='Enter Day', widget=forms.Select(choices=DAYS_OF_WEEK))
