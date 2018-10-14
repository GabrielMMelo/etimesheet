from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q 
from django.contrib.auth.models import User
from django.contrib import messages

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

	return render(request, 'core/index.html', context=context)

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
		name_id = request.POST.getlist('name')
		time = request.POST.getlist('time')
		day = request.POST.getlist('day')

		if name_id != [""]:
			name_id.append(str(request.user.id))

		timetable = None

		if name_id != [""] and time != [""] and day != [""]:
			timetable = TimeTable.objects.filter(
				person__user__id__in=name_id
			).filter(
				time__in=time
			).filter(
				day__in=day
			)
		elif name_id != [""] and time != [""] and day == [""]:
			timetable = TimeTable.objects.filter(
				person__user__id__in=name_id
			).filter(
				time__in=time
			)	
		elif name_id != [""] and time == [""] and day != [""]:
			timetable = TimeTable.objects.filter(
				person__user__id__in=name_id
			).filter(
				day__in=day
			)	
		elif name_id != [""] and time == [""] and day == [""]:
			timetable = TimeTable.objects.filter(
				person__user__id__in=name_id
			)	

		if timetable == None:
			messages.error(request, "Preencha os filtros corretamente! Filtro de nome é obrigatório.")
			return redirect('index')

		context = {
			'timetable': timetable,
		}

	return render(request, 'core/result.html', context=context)