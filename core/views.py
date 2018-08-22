from django.shortcuts import render, redirect
from django.db.models import Q 

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
		name = request.POST['name']
		time = request.POST['time']
		day = request.POST['day']

		timesheet = Timesheet.objects.all()

		if name != None and time != None and day != None:
			timesheet = Timesheet.objects.filter(Q(name__name=name) &
												  Q(time=time) &
												  Q(day=day))
		elif (name != None) and (time == None) and (day == None):
			timesheet = Timesheet.objects.filter(Q(name__name=name))
		elif name == None and time != None and day == None:
			timesheet = Timesheet.objects.filter(Q(time=time))
		elif name == None and time == None and day != None:
			timesheet = Timesheet.objects.filter(Q(day=day))


		context = {
			'timesheet': timesheet,
			'names': Name.objects.all(),
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