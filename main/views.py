from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

from main.forms import NameForm

def init():
	MA = Typ(name='MA', hoehe=33)
	MA.save()
	MC = Typ(name='MC', hoehe=32)
	MC.save()
	MG = Typ(name='MG', hoehe=33)
	MG.save()
	BI = Typ(name='BI', hoehe=33)
	BI.save()
	SO = Typ(name='SO', hoehe=33)
	SO.save()
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
	typen = Typ.objects.all()
	schrank = Kasten.objects.filter(schrank=schranknummer)
	kaesten = {}
	initial = {}
	for i in typen:
		kaesten[i] = Kasten.objects.filter(schrank=schranknummer).filter(typ=i)
		initial[str(i)] = len(kaesten[i])
	
	template = loader.get_template('main/schrank.html')
	# if this is a POST request the form data is processed here
	if request.method == 'POST':
		# creates a form instance and populates it with data from the request
		form = NameForm(request.POST)
		# checks whether it's valid
		print form.errors
		if ( form.is_valid() ):
			for kasten in typen:
				# in case the number of crates of type kasten was reduced
				if (len(kaesten[kasten]) >= form.cleaned_data[str(kasten)]): 
					for i in range(0, len(kaesten[kasten]) - form.cleaned_data[str(kasten)]):
						kaesten[kasten].first().delete()
				# in case the number of crates of type kasten was increased
				elif (len(kaesten[kasten]) <= form.cleaned_data[str(kasten)]):
					for i in range(0,(form.cleaned_data[str(kasten)] - len(kaesten[kasten]))):
						# if there is no matching "schrank" object a new one is created
						if not Schrank.objects.filter(nummer=schranknummer):
							c = Schrank(nummer=schranknummer, hoehe=100)
							c.save()
						b = Kasten(typ=kasten, schrank=Schrank.objects.filter(nummer=schranknummer)[0])
						b.save()
			
			context = RequestContext(request, {'form': form, 'schranknummer': schranknummer})	
			return HttpResponse(template.render(context))
		# if the returned form data is not valid
		else:
			return HttpResponse('Error: you somehow managed to enter invalid data')
	# if it is a GET request a blank form is created
	else:
		form = NameForm(initial)
		context = RequestContext(request, {'form': form, 'schranknummer': schranknummer,})	
		return HttpResponse(template.render(context))
