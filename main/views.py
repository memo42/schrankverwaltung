from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

def schrank(request, schranknummer):
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
