from django.db import models
import requests
import json
from django.utils import timezone
Counter = 100000

class Event(models.Model):
	event_text = models.CharField(max_length=100, default='This is test events')
	event_owner = models.CharField(max_length=100, default='Test owner')
	event_date = models.DateTimeField('Event date', default=timezone.now())
	event_theme = models.CharField(max_length=20, default='Test theme')
	event_city = models.CharField(max_length=30, default='Kazan')
	event_name = models.CharField(max_length=100, default='Test')
	event_address = models.CharField(max_length=100, default='It-lyceum')

	themes = ['Игра', 'Прогулка', 'Другое']
	cities = ['Казань', 'Москва', 'Санкт-Петербург']

	def __str__(self):
		return self.event_text

	def save(self, *args, **kwargs):
		if not self.pk:
			j = ''
			address = self.event_city + ' ' + self.event_address
			request = requests.get("https://geocode-maps.yandex.ru/1.x?geocode={}&apikey=bbbd2d6b-5a52-418a-9cbb-1a4af3d8c88f&format=json".format(address))
			request.encoding = 'utf-8'
			j = json.loads(request.text)
			N, S = (j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
				'lowerCorner']).split(' ')
			N = float(N)
			S = float(S)
			N1, S1 = (j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
				'upperCorner']).split(' ')
			N1 = float(N1)
			S1 = float(S1)
			N += N1
			S += S1
			N /= 2
			S /= 2
			global Counter
			Counter += 1
			with open('events/static/events/data.json', 'r') as file:
				file_text = file.read()
				j = json.loads(file_text)
				j['features'].append({"type": "Feature", "id": Counter, "geometry": {"type": "Point", "coordinates": [S, N]}, "properties": {"balloonContentHeader": "<font size=3><b><a target=\'_blank\' href=\'https://yandex.ru\'>www.vk.com</a></b></font>", "hintContent": self.event_name}})
			with open('events/static/events/data.json', 'w') as file:
				j = json.dump(j, file)
		super(Event, self).save(*args, **kwargs)
