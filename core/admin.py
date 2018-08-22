from django.contrib import admin

from core.models import Timesheet, Name, Role

# Register your models here.

class NameAdmin(admin.ModelAdmin):
	list_display = ('name',)

class RoleAdmin(admin.ModelAdmin):
	list_display = ('role',)

class TimesheetAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'time', 'day')

admin.site.register(Timesheet, TimesheetAdmin)
admin.site.register(Name, NameAdmin)
admin.site.register(Role, RoleAdmin)