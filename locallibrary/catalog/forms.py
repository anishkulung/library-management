from django import forms
import datetime
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import BookInstance
from django.forms import ModelForm


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text='Enter a date between now and 4 weeks(default 3)')

    def clean_renewal_data(self):
        data = self.cleaned_data['renewal_date']

        # check if date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalidate date - renewal in past'))
        # check if date is not more than 4 weeks
        if data > datetime.date.today + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal is more than 4 weeks'))
        return data

# class RenewBookModelForm(ModelForm):

#     def clean_due_back(self):
#         data = self.cleaned_data['due_back']
#         # check if date is not in the past
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalidate date - renewal in past'))
#         # check if date is not more than 4 weeks
#         if data > datetime.date.today + datetime.timedelta(weeks=4):
#             raise ValidationError(
#                 _('Invalid date - renewal is more than 4 weeks'))
#         return data

#     class Meta:
#         model = BookInstance
#         fields = ['due_back']
#         labels = {'due_back': _('New Renewal Date')}
#         help_text = {'due_back': _(
#             'Enter a date between now and 4 weeks(default 3)')}
