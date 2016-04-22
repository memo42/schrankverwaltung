from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

from main.forms import NameForm
from main.forms import TypeForm

import re

def init():
	MA = Typ(name='MA', longname='Mate', hoehe=33)
	MA.save()
	MC = Typ(name='MC', longname='Mate-Cola', hoehe=32)
	MC.save()
	MG = Typ(name='MG', longname='Mate-Granat', hoehe=33)
	MG.save()
	ME = Typ(name='ME', longname='Mate-Eistee', hoehe=33)
	ME.save()
	BI = Typ(name='BI', longname='Bier', hoehe=33)
	BI.save()
	SO = Typ(name='SO', longname='Sonstiges', hoehe=33)
	SO.save()
	LG = Typ(name='LG', longname='Leergut', hoehe=33)
	LG.save()
	# E306
	E3061 = Schrank(nummer='E306.1', raum='E306', hoehe='150')
	E3061.save()
	E3062 = Schrank(nummer='E306.2', raum='E306', hoehe='150')
	E3062.save()
	E3063 = Schrank(nummer='E306.3', raum='E306', hoehe='150')
	E3063.save()
	# E304
	E3041 = Schrank(nummer='E304.1', raum='E304', hoehe='150')
	E3041.save()
	E3042 = Schrank(nummer='E304.2', raum='E304', hoehe='150')
	E3042.save()
	E3043 = Schrank(nummer='E304.3', raum='E304', hoehe='150')
	E3043.save()
	# E303
	E3031 = Schrank(nummer='E303.1', raum='E303', hoehe='150')
	E3031.save()
	E3032 = Schrank(nummer='E303.2', raum='E303', hoehe='150')
	E3032.save()
	E3033 = Schrank(nummer='E303.3', raum='E303', hoehe='150')
	E3033.save()
	# E302
	E3021 = Schrank(nummer='E302.1', raum='E302', hoehe='150')
	E3021.save()
	E3022 = Schrank(nummer='E302.2', raum='E302', hoehe='150')
	E3022.save()
	E3023 = Schrank(nummer='E302.3', raum='E302', hoehe='150')
	E3023.save()
	# E201
	E2011 = Schrank(nummer='E201.1', raum='E201', hoehe='150')
	E2011.save()
	E2012 = Schrank(nummer='E201.2', raum='E201', hoehe='150')
	E2012.save()
	E2013 = Schrank(nummer='E201.3', raum='E201', hoehe='150')
	E2013.save()
	E2014 = Schrank(nummer='E201.4', raum='E201', hoehe='150')
	E2014.save()
	E2015 = Schrank(nummer='E201.5', raum='E201', hoehe='150')
	E2015.save()
	E2016 = Schrank(nummer='E201.6', raum='E201', hoehe='150')
	E2016.save()
	# E013
	E0131 = Schrank(nummer='E013.1', raum='E013', hoehe='1000')
	E0131.save()


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

def uebersicht_nach_sorte(request, sorte):
	typen = Typ.objects.all()
	schraenke = Schrank.objects.all()
	kaesten = Kasten.objects.all()
	raeume = []
	in_room = []
	counter = {}
	for j in schraenke:
		if j.raum not in raeume:
			raeume.append(j.raum)
			#print j.raum
	for k in schraenke:
		in_room.append(Kasten.objects.filter(schrank = k).filter(typ = sorte))
	#	print in_room
	for i in raeume:
		for j in in_room:
			if len(j) > 0 and j[0].schrank.raum == i:
	#			print str(len(j)) + str(j)
				if i in counter:
					counter[i] = counter[i] + len(j)
				else:
					counter.update({i:len(j)})
				#print i + " - " + str(counter[i])
	print counter

	template = loader.get_template('main/uebersicht_nach_sorte.html')
	form = TypeForm(counter)
	context = RequestContext(request, {'form': form, 'sorte': sorte,})
	return HttpResponse(template.render(context))
	#return HttpResponse(raeume)

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
			initial[i.name] = len(kaesten[i])
		template = loader.get_template('main/schrank.html')
		# if this is a POST request the form data is processed here
		if request.method == 'POST':
			# creates a form instance and populates it with data from the request
			form = NameForm(request.POST)
			success = ''
			# checks whether it's valid
			# print form.errors
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
						for i in range(0, (form.cleaned_data[str(kasten)] - len(kaesten[kasten]))):
							b = Kasten(typ=kasten, schrank=Schrank.objects.filter(nummer=schranknummer)[0])
							b.save()
				context = RequestContext(request, {'form': form, 'schranknummer': schranknummer, 'success': success, 'room': room, 'next_cupboard': next_cupboard, 'previous_cupboard': previous_cupboard,})

				if 'previous' in request.POST:
					template.render(context)
					#return HttpResponse(template.render(context))
					return HttpResponseRedirect("../" + str(room) + "." + str(previous_cupboard))
				elif 'next' in request.POST:
					template.render(context)
					return HttpResponseRedirect("../" + str(room) + "." + str(next_cupboard))
				else:
					return HttpResponse(template.render(context))
			# if the returned form data is not valid
			else:
				return HttpResponse('Error: you somehow managed to enter invalid data')

		# if it is a GET request a blank form is created
		else:
			form = NameForm(initial)
			context = RequestContext(request, {'form': form, 'schranknummer': schranknummer, 'room': room, 'next_cupboard': next_cupboard, 'previous_cupboard': previous_cupboard,})
			return HttpResponse(template.render(context))

	else:
		return HttpResponse('Error: not a valid cupboard')
