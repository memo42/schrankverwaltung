from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.context_processors import csrf

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

from main.forms import NameForm

import re

def init():
	MA = Typ(name='MA', hoehe=33)
	MA.save()
	MC = Typ(name='MC', hoehe=32)
	MC.save()
	MG = Typ(name='MG', hoehe=33)
	MG.save()
	ME = Typ(name='ME', hoehe=33)
	ME.save()
	BI = Typ(name='BI', hoehe=33)
	BI.save()
	Sonstiges = Typ(name='Sonstiges', hoehe=33)
	Sonstiges.save()
	LG = Typ(name='LG', hoehe=33)
	LG.save()

# Reads the total number of crates in each category from the database and passes the count to the uebersicht template.
def uebersicht(request):
	typen = Typ.objects.all()
	if not typen :
		init()
	kaesten = {}
	initial = {}
	for i in typen:
		kaesten[i] = Kasten.objects.filter(typ=i)
		initial[str(i)] = len(kaesten[i])

	template = loader.get_template('main/uebersicht.html')
	form = NameForm(initial)
	context = RequestContext(request, {'form': form,})
	return HttpResponse(template.render(context))

# Reads the total number of crates in each category per room from the database and passes it to the uebersicht template.
def raum_uebersicht(request, raumnummer):
	typen = Typ.objects.all()
	schraenke = Schrank.objects.filter(raum=raumnummer)
	kaesten = {}
	initial = {}
	for i in typen:
		kaesten[i] = []
		for j in schraenke:
			temp = Kasten.objects.filter(typ=i).filter(schrank=j)
			for k in temp:
				kaesten[i].append(k)
		initial[str(i)] = len(kaesten[i])

	template = loader.get_template('main/uebersicht.html')
	form = NameForm(initial)
	context = RequestContext(request, {'form': form, 'raumnummer': raumnummer,})
	return HttpResponse(template.render(context))

# Reads the number of crates in one part of the cupboard, displays them and lets the user change them.
def schrank(request, schranknummer):

	# if there is no matching "schrank" object throw error
	if Schrank.objects.filter(nummer=schranknummer):
		typen = Typ.objects.all()
		schrank = Kasten.objects.filter(schrank=schranknummer)
		kaesten = {}
		initial = {}

		m = re.search('(?<=[A-Z][0-9]{3}.)[0-9]', schranknummer)
		single_digit_number = m.group(0)
		m = re.search('(?=.[0-9])[A-Z][0-9]{3}', schranknummer)
		room = m.group(0)

		in_room = Schrank.objects.filter(raum = room)

		next_cupboard = ((int(single_digit_number)) % len(in_room)) + 1
		previous_cupboard = ((int(single_digit_number) - 2) % len(in_room)) + 1

		for i in typen:
			kaesten[i] = Kasten.objects.filter(schrank=schranknummer).filter(typ=i)
			initial[str(i)] = len(kaesten[i])
		template = loader.get_template('main/schrank.html')
		# if this is a POST request the form data is processed here
		if request.method == 'POST':
			# cross site request forgery protection
			csrf = {}
			csrf.update(csrf(request))
			# creates a form instance and populates it with data from the request
			form = NameForm(request.POST)
			success = ''

			# checks whether it's valid
			#print form.errors
			if ( form.is_valid() ):
				for kasten in typen:
					# in case the number of crates of type kasten was reduced
					if (len(kaesten[kasten]) > form.cleaned_data[str(kasten)]):
						success = 'Saved'
						for i in range(0, len(kaesten[kasten]) - form.cleaned_data[str(kasten)]):
							kaesten[kasten].first().delete()
					# in case the number of crates of type kasten was increased
					elif (len(kaesten[kasten]) < form.cleaned_data[str(kasten)]):
						success = 'Saved'
						for i in range(0,(form.cleaned_data[str(kasten)] - len(kaesten[kasten]))):
							b = Kasten(typ=kasten, schrank=Schrank.objects.filter(nummer=schranknummer)[0])
							b.save()

				context = RequestContext(request, {'form': form, 'schranknummer': schranknummer, 'success': success, 'room': room, 'next_cupboard': next_cupboard, 'previous_cupboard': previous_cupboard, 'csrf': csrf})
				return HttpResponse(template.render(context))
			# if the returned form data is not valid
			else:
				return HttpResponse('Error: you somehow managed to enter invalid data')
		# if it is a GET request a blank form is created
		else:
			form = NameForm(initial)
			context = RequestContext(request, {'form': form, 'schranknummer': schranknummer, 'room':room, 'next_cupboard': next_cupboard, 'previous_cupboard': previous_cupboard,})
			return HttpResponse(template.render(context))

	else:
		return HttpResponse('Error: not a valid cupboard')
