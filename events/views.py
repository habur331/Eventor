from django.shortcuts import render
from .models import Event


# Create your views here.
def index(request):
	return render(request, 'events/index.html', context={'cities': Event.cities, 'themes': Event.themes, 'events': Event.objects.all()})
