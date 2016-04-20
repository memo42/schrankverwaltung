from django import forms
from django.core import validators
from django.utils.safestring import mark_safe

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

maxAnzahl = 100
class NameForm(forms.Form):
	typ = Typ.objects.all()
	if len(typ) > 0:
		myLabel = {}
		myFormElement = {}
		for i in typ:
			myLabel[i.name] = mark_safe('<a href="/main/' + i.name + '">' + i.longname + '</a>')

		a = forms.IntegerField(label=myLabel[typ[0].name], widget=forms.TextInput(attrs={'name': typ[0].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		b = forms.IntegerField(label=myLabel[typ[1].name], widget=forms.TextInput(attrs={'name': typ[1].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		c = forms.IntegerField(label=myLabel[typ[2].name], widget=forms.TextInput(attrs={'name': typ[2].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		d = forms.IntegerField(label=myLabel[typ[3].name], widget=forms.TextInput(attrs={'name': typ[3].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		e = forms.IntegerField(label=myLabel[typ[4].name], widget=forms.TextInput(attrs={'name': typ[4].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		f = forms.IntegerField(label=myLabel[typ[5].name], widget=forms.TextInput(attrs={'name': typ[5].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])
		g = forms.IntegerField(label=myLabel[typ[6].name], widget=forms.TextInput(attrs={'name': typ[6].name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }), validators = [validators.MaxValueValidator(maxAnzahl)])

class TypeForm(forms.Form):
	schraenke = Schrank.objects.all()
	if len(schraenke) > 0:
		raeume = []
		in_room = []
		for j in schraenke:
			if j.raum not in raeume:
				raeume.append(j.raum)
				print j.raum
		myLabel = {}
		for i in raeume:
			myLabel[i] = mark_safe('<a href="/main/' + i + '">' + i + '</a>')
		a = forms.IntegerField(label=myLabel[raeume[0]], widget=forms.TextInput(attrs={'name': raeume[0], 'class': "form-control input-number"}))
		b = forms.IntegerField(label=myLabel[raeume[1]], widget=forms.TextInput(attrs={'name': raeume[1], 'class': "form-control input-number"}))
		c = forms.IntegerField(label=myLabel[raeume[2]], widget=forms.TextInput(attrs={'name': raeume[2], 'class': "form-control input-number"}))
		d = forms.IntegerField(label=myLabel[raeume[3]], widget=forms.TextInput(attrs={'name': raeume[3], 'class': "form-control input-number"}))
		e = forms.IntegerField(label=myLabel[raeume[4]], widget=forms.TextInput(attrs={'name': raeume[4], 'class': "form-control input-number"}))
		f = forms.IntegerField(label=myLabel[raeume[5]], widget=forms.TextInput(attrs={'name': raeume[5], 'class': "form-control input-number"}))
