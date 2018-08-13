from django.contrib import admin

from .models import Timesheet

# Register your models here.

class TimesheetAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'time', 'day')

admin.site.register(Timesheet, TimesheetAdmin)