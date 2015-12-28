from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	# example: /main/
	url(r'^$', views.uebersicht, name='uebersicht'),
	# example: /main/MA/
	url(r'^(?P<sorte>[a-zA-Z]{2})/$', views.uebersicht_nach_sorte, name='Uebersicht'),
	# example: /main/e306/
	url(r'^(?P<raumnummer>E[0-9a-zA-Z]{3})/$', views.raum_uebersicht, name='Raumuebersicht'),
	# example: /main/e306.1/
	url(r'^(?P<schranknummer>E[0-9a-zA-Z]{3}\.\d)/$', views.schrank, name='Schrankuebersicht'),
)
