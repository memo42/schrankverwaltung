from django.db import models

class Typ(models.Model):
	name = models.CharField('Inhalt des Kastens (Abkuerzung)',
									max_length=2,
									primary_key=True)
	longname = models.CharField('Inhalt des Kastens (lang)', max_length=20)
	hoehe = models.IntegerField('Hoehe des Kastens in Millimeter (mm)')

	def __unicode__(self):
		return u'%s' % (self.longname)

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
