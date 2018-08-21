from django.db import models

# Create your models here.

class Timesheet(models.Model):
	ROLE_CHOICE = (
		('Coordenador', 'Coordenador'),
		('Diretor Presidente', 'Diretor Presidente'),
		('Diretor Vice-Presidente', 'Diretor Vice-Presidente'),
		('Diretor de Projetos', 'Diretor de Projetos'),
		('Gerente de Projetos', 'Gerente de Projetos'),
		('Diretor de Negócios', 'Diretor de Negócios'),
		('Gerente de Marketing', 'Gerente de Marketing'),
		('Diretor de Processos Internos', 'Diretor de Processos Internos'),
		('Gerente de Produtos Internos', 'Gerente de Produtos Internos'),
		('Membro', 'Membro'),
	)

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

	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100, choices=ROLE_CHOICE)
	time = models.CharField(max_length=10, choices=TIME_CHOICE)
	day = models.CharField(max_length=10, choices=DAY_CHOICE)
	row = models.IntegerField()
	column = models.IntegerField()