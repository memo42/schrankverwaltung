from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

def schrank(request, schranknummer):
	schrank = Schrank.objects.get(nummer="E306.1")
	#template = loader.get_template('main/index.html')
	#return render(request, 'main/new.html')
	return HttpResponse("%s" % schrank.kaesten.typ)
def uebersicht(request):
	return HttpResponse("Uebersicht") 
