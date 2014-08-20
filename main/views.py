from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

from main.forms import NameForm

def schrank(request, schranknummer):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponse("thanks")
	else:
		typen = Typ.objects.all()
		schrank = Kasten.objects.filter(schrank=schranknummer)
		kaesten = [42]
		kaesten.pop()
		for i in typen:
			kaesten.append(Kasten.objects.filter(schrank=schranknummer).filter(typ=i))
		#for name in typ:
		#	typen = schrank.filter(schrank__typ=name)		
	
		template = loader.get_template('main/index.html')
		context = RequestContext(request, {'schrank': schrank, 'kaesten': kaesten, 'typen': typen, })
		return HttpResponse(template.render(context))
		#return render(request, 'main/new.html')
		#return HttpResponse("%s" % schrank)
def uebersicht(request):
	return HttpResponse("Uebersicht")
def get_name(request, schranknummer):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		print form.errors
		if form.is_valid():
			mate = form.cleaned_data['mate']
			mategranat = form.cleaned_data['mateGranat']
			matecola = form.cleaned_data['mateCola']
			
			# process the data in form.cleaned_data as required
			# ...
			# respond with a friendly thank you.:
			return HttpResponse(mate + mategranat)
		else:
			return HttpResponse('no')
	# if a GET (or any other method) we'll create a blank form
	else:
		typen = Typ.objects.all()
		schrank = Kasten.objects.filter(schrank=schranknummer)
		kaesten = [42]
		kaesten.pop()
		for i in typen:
			kaesten.append(Kasten.objects.filter(schrank=schranknummer).filter(typ=i))
		initial = {'mate' : '0', 'mateCola' : '0', 'mateGranat' : '0', 'bier' : '0', 'sonstiges' : '0', 'leergut' : '0'}
		for kasten in kaesten:
			#initial[kasten.typ] = len(kasten)
			print kasten
			print '1'
		form = NameForm(initial)
#={kaesten[0][0].name: len(kaesten[0]), 'mateGranat': len(kaesten[1]), 'mateCola': len(kaesten[2])})

		template = loader.get_template('main/name.html')
		context = RequestContext(request, {'form': form, 'schrank': schrank, 'kaesten': kaesten, 'typen': typen, 'schranknummer': schranknummer,})	

		return HttpResponse(template.render(context))
