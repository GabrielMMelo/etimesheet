from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q 
from django.contrib.auth.models import User

from core.forms import TimeTable
from core.models import Person, TimeTable
# Create your views here.

@login_required
def index(request):
	if request.method == "GET":
		person = Person.objects.get(user=request.user.id)
		context = {
			'person': person,
			'timetable': TimeTable.objects.filter(person=person.id),
			'users': User.objects.all().exclude(is_superuser=True)
		}

	return render(request, 'core/info.html', context=context)

@login_required
@require_POST
def save(request):
	if request.method == "POST":
		p = Person.objects.get(user=request.user.id)

		t = TimeTable()
		t.person = p
		t.row = request.POST['row']
		t.column = request.POST['column']
		t.day = request.POST['day']
		t.time = request.POST['time']
		t.save()
	
	return redirect('index')

@login_required
@require_POST
def delete(request):
	if request.method == "POST":
		p = Person.objects.get(user=request.user.id)

		row = request.POST['row']
		column = request.POST['column']

		t = TimeTable.objects.filter(
				person=p.id
			).filter(
				row=row
			).filter(
				column=column
			)
		t.delete()
		
	return redirect('index')

@login_required
@require_POST
def result(request):
	if request.method == "POST":
		name = request.POST['name']

		timetable = TimeTable.objects.filter(
			person__user__id__in=[name, request.user.id]
		)

		context = {
			'timetable': timetable,
		}
	return render(request, 'core/result.html', context=context)