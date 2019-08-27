"""Forms needed to library app."""

import datetime  as dt

from django import forms
from django.core.exceptions import ValidationError
#from.models import Book_Instance

class RnewDueBack(forms.Form):
    """Form to renew due back of book instance."""

    due_back = forms.DateField(
        label='Renew Date', 
        label_suffix=':',
        help_text='renew date must be max three weeks.')

    # customized validation
    def clean_due_back(self):
        """checks if new date is in the past or more than 3 weeks."""

        due_back = self.cleaned_data['due_back']

        if due_back < dt.date.today():
            raise ValidationError('old renew date')

        if due_back > dt.date.today()+dt.timedelta(weeks=4):
            raise ValidationError('New date is larger than 4 weeks!!')
        
        return due_back