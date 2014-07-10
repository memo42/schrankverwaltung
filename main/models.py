from django.db import models

class Typ(models.Model):
	NAME_CHOICES = (
		('MA', 'Mate'),
		('MC', 'Mate-Cola'),
		('MG', 'Mate-Granat'),
		('SO', 'sonstiges'),
	)
	name = models.CharField('Inhalt des Kastens', 
									max_length=2,
									choices=NAME_CHOICES,
									default='SO',
									primary_key=True)
	hoehe = models.IntegerField('Hoehe des Kastens in Millimeter (mm)')

	def __unicode__(self): 
		return self.name

class Kasten(models.Model):
	ID = models.IntegerField('ID des Kastens', default=0, primary_key=True)
	voll = models.BooleanField('Status des Kastens')
	typ = models.ForeignKey(Typ)
	
	def __unicode__(self):
		return u'%s %s' % (self.typ, self.voll)

class Schrank(models.Model):
	nummer = models.CharField('eineindeutige SchrankNummer. Format E306.1', max_length=6, default=0, primary_key=True)
	raum = models.CharField('Raum wo Schrank steht', max_length=6)
	kaesten = models.ForeignKey(Kasten)

	def __unicode__(self): 
		return u'%s' % (self.nummer)
