from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
import json
from .models import Event
import datetime


# Create your views here.
def index(request):
	if request.POST:
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

		return render(request, 'events/event.html', context={'event_list': event_list})
	return render(request, 'events/index.html', context={'cities': Event.cities, 'themes': Event.themes,
														 'events': get_list_or_404(Event.objects.all())})
