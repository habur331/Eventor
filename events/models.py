from django.db import models


class Event(models.Model):
	event_text = models.CharField(max_length=100)
	event_owner = models.CharField(max_length=100)
	event_date = models.DateTimeField('Event date')
	event_theme = models.CharField(max_length=20, default='Without theme')
	event_city = models.CharField(max_length=30)
	event_name = models.CharField(max_length=100)
	event_address = models.CharField(max_length=100)

	themes = ['game', 'walk', 'other']
	cities = ['Kazan', 'Moscow', 'Saint-Petersburg']

	def __str__(self):
		return self.event_text
