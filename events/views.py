from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
import json
from .forms import CreateEventForm
from .models import Event
import datetime
import requests
import json


def index(request):
	Event.create_json()
	if request.POST:
		if request.POST.get('request') == 'search':
			city = request.POST.getlist('city[]')
			theme = request.POST.getlist('theme[]')
			date_start = request.POST.get('date_start')
			date_end = request.POST.get('date_end')

			event_list = Event.objects.all()
			if city:
				event_list = event_list.filter(event_city__in=city)
			if theme:
				event_list = event_list.filter(event_theme__in=theme)
			if date_end:
				event_list = event_list.filter(event_date__lte=date_end)
			if date_start:
				event_list = event_list.filter(event_date__gte=date_start)


			Event.create_json()
			return render(request, 'events/event.html', context={'event_list': event_list, 'request': request})


		elif request.POST.get('request') == 'info':
			pk = request.POST.get('pk')
			Event.create_json()
			return render(request, 'events/info.html', context={'event': Event.objects.get(pk=pk), 'request': request})

		elif request.POST.get('request') == 'edit':
			pk = request.POST.get('pk')
			Event.create_json()
			return render(request, 'events/event.html',
						  context={'event_list': Event.objects.get(pk=pk), 'request': request})

		elif request.POST.get('request') == 'delete':
			pk = request.POST.get('pk')
			Event.objects.get(pk=pk).delete()
			event_list = Event.objects.all()
			print(event_list)
			Event.create_json()
			return render(request, 'events/event.html', context={'event_list': event_list, 'request': request})

		elif request.POST.get('request') == 'singup':
			redirect('events/index.html', context={'cities': Event.cities, 'themes': Event.themes,
												   'event_list': Event.objects.all(),
												   'form': CreateEventForm,
												   'request': request})

		else:
			text = request.POST.get('event_text')
			city = request.POST.get('event_city')
			address = request.POST.get('event_address')
			name = request.POST.get('event_name')
			theme = request.POST.get('event_theme')
			datetime = request.POST.get('event_datetime')
			owner = '79534800552'

			new_event = Event.objects.create(event_text=text, event_city=city, event_address=address, event_name=name,
											 event_theme=theme, event_date=datetime, event_owner=owner)
			new_event.save()

			redirect('events/index.html', context={'cities': Event.cities, 'themes': Event.themes,
												   'event_list': Event.objects.all(),
												   'form': CreateEventForm,
												   'request': request})

	event_list = Event.objects.all()
	Event.create_json()
	return render(request, 'events/index.html', context={'cities': Event.cities, 'themes': Event.themes,
														 'event_list': event_list,
														 'form': CreateEventForm,
														 'request': request})
