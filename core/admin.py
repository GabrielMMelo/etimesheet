from django.contrib import admin

from core.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	list_display = ('role', )

admin.site.register(Person, PersonAdmin)