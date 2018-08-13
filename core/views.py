from django.shortcuts import render

from .models import Timesheet
# Create your views here.

def index(request):
	if request.method == "GET":
		context = {
			'timesheet': Timesheet.objects.all()
		}
	else:
		context = {

		}
	return render(request, 'core/index.html', context=context)
