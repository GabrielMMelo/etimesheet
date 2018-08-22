from django.shortcuts import render, redirect
from core.forms import TimesheetForm

from core.models import Timesheet, Name, Role
# Create your views here.

def index(request):
	if request.method == "GET":
		context = {
			'timesheet': Timesheet.objects.all(),
			'names': Name.objects.all()
		}
	else:
		context = {

		}
	return render(request, 'core/info.html', context=context)

def save(request):
	form = TimesheetForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.row = request.POST['row']
			model_instance.column = request.POST['column']
			model_instance.save()
			return redirect('index')

	context = {
		'names': Name.objects.all(),
		'roles': Role.objects.all(),
		'form': form,
	}
	return render(request, 'core/save.html', context=context)