import datetime

from django import forms
from django.forms import DateInput

from .models import Event


def create_choices(array):
	result = []
	for elem in array:
		result.append((elem, elem))
	return result


class CreateEventForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control selectpicker'
			visible.field.widget.attrs['data-live-search'] = 'true'

	event_text = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'rows': 4}))
	event_owner = forms.CharField(label="", initial='+79534800552')
	event_datetime = forms.DateTimeField(widget=DateInput(attrs={'type': 'datetime-local'}),
										 initial=datetime.date.today(), localize=True)
	event_theme = forms.ChoiceField(label="Тема", choices=create_choices(Event.themes))
	event_city = forms.ChoiceField(label="Город", choices=create_choices(Event.cities))
	event_name = forms.CharField(label="Название")
	event_address = forms.CharField(label="Адрес")
