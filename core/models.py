from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .logger import Logger

# Create your models here.

TIME_CHOICE = (
	('07:00', '07:00'),
	('08:00', '08:00'),
	('09:00', '09:00'),
	('10:00', '10:00'),
	('11:00', '11:00'),
	('12:00', '12:00'),
	('13:00', '13:00'),
	('14:00', '14:00'),
	('15:00', '15:00'),
	('16:00', '16:00'),
	('17:00', '17:00'),
	('18:00', '18:00'),
	('19:00', '19:00'),
	('20:00', '20:00'),
	('21:00', '21:00'),
	('22:00', '22:00'),
)

DAY_CHOICE = (
	('Dom', 'Dom'),
	('Seg', 'Seg'),
	('Ter', 'Ter'),
	('Qua', 'Qua'),
	('Qui', 'Qui'),
	('Sex', 'Sex'),
	('Sáb', 'Sáb'),
)

class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class TimeTable(models.Model):
	time = models.CharField(max_length=10, choices=TIME_CHOICE)
	day = models.CharField(max_length=10, choices=DAY_CHOICE)
	row = models.IntegerField()
	column = models.IntegerField()
	person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


def save_log(sender, instance, **kwargs):
	log = Logger.get_instance()
	log.info('{} salvou um horario no dia {} {}'.format(instance.person.user.username, instance.day, instance.time))
post_save.connect(save_log, sender=TimeTable)


def delete_log(sender, instance, **kwargs):
	log = Logger.get_instance()
	log.info('{} deletou um horario no dia {} {}'.format(instance.person.user.username, instance.day, instance.time))
post_delete.connect(delete_log, sender=TimeTable)
