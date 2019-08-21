from django.db import models
import requests
import json
from django.utils import timezone


class Event(models.Model):
	event_text = models.CharField(max_length=100, default='This is test events')
	event_owner = models.CharField(max_length=100, default='Test owner')
	event_date = models.DateTimeField('Event date', default=timezone.now())
	event_theme = models.CharField(max_length=20, default='Test theme')
	event_city = models.CharField(max_length=30, default='Kazan')
	event_name = models.CharField(max_length=100, default='Test')
	event_address = models.CharField(max_length=100, default='It-lyceum')
	event_participant = models.IntegerField(default=0)
	event_coordinates1 = models.CharField(max_length=100, default='0')
	event_coordinates2 = models.CharField(max_length=100, default='0')

	def create_address(self):
		address = self.event_city + ' ' + self.event_address
		request = requests.get(
			"https://geocode-maps.yandex.ru/1.x?geocode={}&apikey=bbbd2d6b-5a52-418a-9cbb-1a4af3d8c88f&format=json".format(
				address))
		request.encoding = 'utf-8'
		j = json.loads(request.text)
		request.encoding = 'utf-8'
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
		self.event_coordinates1 = S
		self.event_coordinates2 = N
		self.save()

	@staticmethod
	def create_json():
		event = Event.objects.all()
		with open('events/static/events/data.json', 'r') as file:
			file_text = file.read()
			j = json.loads(file_text)
			j['features'] = []
			for e in event:
				Event.create_address(e)
				j['features'].append({"type": "Feature", "id": e.pk, "geometry": {"type": "Point", "coordinates": [
					float(e.event_coordinates1), float(e.event_coordinates2)]},
									  "properties": {"hintContent": e.event_name}})
		with open('events/static/events/data.json', 'w') as file:
			json.dump(j, file)

	themes = ['Выставки',
			  'Фестивали',
			  'Гранты',
			  'Концерты',
			  'Творческие встречи',
			  'Мастер-классы',
			  'Кинопоказы', ]

	cities = ['Агрыз', 'Азнакаево', 'Аксубаево', 'Актюбинский', 'Алексеевское', 'Альметьевск', 'Апастово', 'Арск',
			  'Балтаси', 'Бавлы', 'Богатые', 'Сабы', 'Болгар', 'Бугульма', 'Буинск', 'Васильево', 'Джалиль', 'Елабуга',
			  'Заинск', 'Зеленодольск', 'Камские Поляны', 'Камское Устье', 'Карабаш', 'Казань', 'Куйбышевский Затон',
			  'Кукмор', 'Лаишево', 'Лениногорск', 'Мамадыш', 'Менделеевск',' Мензелинск', 'Набережные Челны', 'Нижнекамск',
			  'Нижние Вязовые', 'НижняяМактама', 'Нурлат', 'РыбнаяСлобода', 'Тенишево', 'Тетюши', 'Уруссу', 'Чистополь']

	def __str__(self):
		return self.event_text
