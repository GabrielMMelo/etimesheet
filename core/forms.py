from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from core.models import Person, TimeTable

class PersonForm(forms.Form):
	first_name = forms.CharField(label='Primeiro nome')
	last_name = forms.CharField(label='Segundo nome')
	cargo = forms.CharField(label='Cargo')

	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']	
		user.last_name = self.cleaned_data['last_name']
		user.save()
		
		person = Person()
		person.role = self.cleaned_data['cargo']
		person.user = user
		person.save()