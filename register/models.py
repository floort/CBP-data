from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name

# Create your models here.
class Company(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return self.name
    def link(self):
        return "<a href=\"%s\">Link</a>" % (self.url)
    name.allow_tags=True
    link.allow_tags=True

    def tags_str(self):
        if not self.tags: return ""
        return ", ".join([t.__unicode__() for t in self.tags.iterator()])
Company.verbose_name = "Bedrijf"
Company.verbose_name_plural = "Bedrijven"

class Melding(models.Model):
    cbpid = models.IntegerField()
    company = models.ForeignKey(Company)
    description = models.CharField(max_length=255)
    doorgifte_passend = models.CharField(max_length=8, choices=(
        ("Y","Ja"),
        ("N","Nee"),
        ("?","Onbekend")))
    url = models.URLField()
    doorgifte_buiten_eu = models.BooleanField()
    naam = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return self.naam
    
    def link(self):
        return u'<a href=%s>link</a>' % (self.url)
    link.allow_tags = True
Melding.verbose_name = "Melding"
Melding.verbose_name_plural = "Meldingen"

class Betrokkene(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)

	def __unicode__(self):
		return self.naam
Betrokkene.verbose_name = "Betrokkene"
Betrokkene.verbose_name_plural = "Betrokkenen"

class BetrokkeneDetails(models.Model):
	naam = models.CharField(max_length=255)
	omschrijving = models.CharField(max_length=1024)
	betrokkene = models.ForeignKey(Betrokkene)

	def __unicode__(self):
		return self.naam
BetrokkeneDetails.verbose_name = "Betrokkene Details"
BetrokkeneDetails.verbose_name_plural = "Betrokkene Details"

class Ontvanger(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)

	def __unicode__(self):
		return self.naam
Ontvanger.verbose_name = "Ontvanger"
Ontvanger.verbose_name_plural = "Ontvangers"

class Verantwoordelijke(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)
	bezoekadres = models.TextField()
	
	def __unicode__(self):
		return self.naam
Verantwoordelijke.verbose_name = "Verantwoordelijke"
Verantwoordelijke.verbose_name_plural = "Verantwoordelijken"

class Doel(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.naam
Doel.verbose_name = "Doel"
Doel.verbose_name_plural = "Doelen"


