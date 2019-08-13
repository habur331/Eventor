from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
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
			event_list.filter(event_city=city)
		if theme:
			event_list.filter(event_theme=theme)
		if date_start:
			date_start = datetime.date(date_start.split('-')[0], date_start.split('-')[1], date_start.split('-')[2])

		print(event_list)
		print(date_start)
		return HttpResponse(event_list)
	return render(request, 'events/index.html', context={'cities': Event.cities, 'themes': Event.themes,
														 'events': get_list_or_404(Event.objects.all())})
