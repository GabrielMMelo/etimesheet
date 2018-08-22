from django.forms import ModelForm
from core.models import Timesheet

class TimesheetForm(ModelForm):
	class Meta:
		model = Timesheet
		exclude = ('row', 'column')