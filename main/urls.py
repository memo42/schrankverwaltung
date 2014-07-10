from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	# example: /main/	
	url(r'^$', views.uebersicht, name='uebersicht'),
	# example: /main/e306.1/
	url(r'^(?P<schranknummer>E\d+.\d)/$', views.schrank, name='Schrankuebersicht'),
)
