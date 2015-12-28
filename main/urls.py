from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	# example: /main/
	url(r'^$', views.uebersicht, name='uebersicht'),
	# example: /main/MA/
	url(r'^(?P<sorte>[a-zA-Z]+)/$', views.uebersicht_nach_sorte, name='Uebersicht'),
	# example: /main/e306/
	url(r'^(?P<raumnummer>[0-9a-zA-Z]+)/$', views.raum_uebersicht, name='Raumuebersicht'),
	# example: /main/e306.1/
	url(r'^(?P<schranknummer>[0-9a-zA-Z]+\.\d)/$', views.schrank, name='Schrankuebersicht'),
)
