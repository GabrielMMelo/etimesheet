from django.shortcuts import render, redirect

from .models import Timesheet
# Create your views here.

def index(request):
	if request.method == "GET":
		context = {
			'timesheet': Timesheet.objects.all(),

			#all names without duplicate value
			'names': Timesheet.objects.all().distinct('name')
		}
	else:
		context = {

		}
	return render(request, 'core/info.html', context=context)

def save(request):
	# try using form or model form
	if request.method == "POST":
		name = request.POST.get('name')
		time = request.POST.get('time')
		day = request.POST.get('day')
		role = request.POST.get('role')
		row = request.POST.get('row')
		column = request.POST.get('column')
		t = Timesheet(name=name, role=role, time=time, day=day, row=row, column=column)
		t.save()

		return redirect('index')

	context = {
		'timesheet': Timesheet.objects.all(),

		#all names without duplicate value
		'names': Timesheet.objects.all().distinct('name')
	}
	return render(request, 'core/save.html', context=context)