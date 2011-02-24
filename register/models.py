from django.db import models

# Create your models here.
class Company(models.Model):
	url = models.URLField(unique=True)
	name = models.CharField(max_length=127)
	meldingen = models.ManyToManyField('Melding')

	def __unicode__(self):
		return self.name
	def link(self):
		return "<a href=\"%s\">Link</a>" % (self.url)
	name.allow_tags=True
	link.allow_tags=True

class Melding(models.Model):
	cbpid = models.IntegerField()
	description = models.CharField(max_length=127)
	doorgifte_passend = models.CharField(max_length=8, choices=(
		("Y","Ja"),
		("N","Nee"),
		("?","Onbekend")))
	url = models.URLField()
	doorgifte_buiten_eu = models.BooleanField()
	naam = models.CharField(max_length=127)
	
	def __unicode__(self):
		return self.naam
	

class Betrokkene(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=127)

	def __unicode__(self):
		return self.naam

class BetrokkeneDetails(models.Model):
	naam = models.CharField(max_length=127)
	omschrijving = models.CharField(max_length=1024)
	betrokkene = models.ForeignKey(Betrokkene)

	def __unicode__(self):
		return self.naam

class Ontvanger(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=127)

	def __unicode__(self):
		return self.naam

class Verantwoordelijke(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=127)
	bezoekadres = models.TextField()
	
	def __unicode__(self):
		return self.naam

class Doel(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=127)
	
	def __unicode__(self):
		return self.naam




