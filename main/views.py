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
			return HttpRespons("thanks")
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
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'main/name.html', {'form': form})
