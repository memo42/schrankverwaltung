from django.db import models

class Typ(models.Model):
	NAME_CHOICES = (
		('MA', 'Mate'),
		('MC', 'Mate-Cola'),
		('MG', 'Mate-Granat'),
		('BI', 'Bier'),
		('SO', 'Sonstiges'),
		('LG', 'Leergut'),
	)
	name = models.CharField('Inhalt des Kastens', 
									max_length=2,
									choices=NAME_CHOICES,
									default='SO',
									primary_key=True)
	hoehe = models.IntegerField('Hoehe des Kastens in Millimeter (mm)')

	def __unicode__(self): 
		return u'%s' % (self.name)

class Schrank(models.Model):
	nummer = models.CharField('eineindeutige SchrankNummer. Format E306.1', max_length=6, default=0, primary_key=True)
	raum = models.CharField('Raum in dem der Schrank steht', max_length=4)
	hoehe = models.IntegerField('Hoehe des Schrankes', default=0)

	def __unicode__(self): 
		return u'%s' % (self.nummer)

class Kasten(models.Model):
	typ = models.ForeignKey(Typ)
	schrank = models.ForeignKey(Schrank)
	
	def __unicode__(self):
		return u'%s %s' % (self.typ, self.schrank)

