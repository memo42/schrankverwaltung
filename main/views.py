from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

from main.forms import NameForm

def schrank(request, schranknummer):
	typen = Typ.objects.all()
	schrank = Kasten.objects.filter(schrank=schranknummer)
	kaesten = {}
	initial = {}
	for i in typen:
		kaesten[i] = Kasten.objects.filter(schrank=schranknummer).filter(typ=i)
		initial[str(i)] = len(kaesten[i])
	
	template = loader.get_template('main/name.html')
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		print form.errors
		if ( form.is_valid() ):
			for kasten in typen:
				print len(kaesten[kasten])
				print form.cleaned_data[str(kasten)]
				#if ( len(kaesten[kasten]) == form.cleaned_data[str(kasten)]):
				#	print "gleich"
				if (len(kaesten[kasten]) >= form.cleaned_data[str(kasten)]): 
					#print "weniger"
					for i in range(0, len(kaesten[kasten]) - form.cleaned_data[str(kasten)]):
						print kaesten[kasten].first().delete()
				elif (len(kaesten[kasten]) <= form.cleaned_data[str(kasten)]):
					#print "mehr"
					for i in range(0,(form.cleaned_data[str(kasten)] - len(kaesten[kasten]))):
						if Schrank.objects.filter(nummer=schranknummer):
							b = Kasten(typ=kasten, schrank=Schrank.objects.filter(nummer=schranknummer)[0])
							b.save()
						else:
							c = Schrank(nummer=schranknummer, hoehe=100)
							c.save()
							b = Kasten(typ=kasten, schrank=Schrank.objects.filter(nummer=schranknummer)[0])
							b.save()
			
			context = RequestContext(request, {'form': form, 'schrank': schrank, 'kaesten': kaesten, 'typen': typen, 'schranknummer': schranknummer,})	
			return HttpResponse(template.render(context))
		else:
			return HttpResponse('no')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm(initial)
		context = RequestContext(request, {'form': form, 'schrank': schrank, 'kaesten': kaesten, 'typen': typen, 'schranknummer': schranknummer,})	
		return HttpResponse(template.render(context))
