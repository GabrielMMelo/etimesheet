from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
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
			'users': User.objects.values_list('first_name')
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

def delete(request):
	return redirect('index')

