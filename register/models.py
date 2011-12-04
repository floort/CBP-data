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

class Betrokkene(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)

	def __unicode__(self):
		return self.naam

class BetrokkeneDetails(models.Model):
	naam = models.CharField(max_length=255)
	omschrijving = models.CharField(max_length=1024)
	betrokkene = models.ForeignKey(Betrokkene)

	def __unicode__(self):
		return self.naam

class Ontvanger(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)

	def __unicode__(self):
		return self.naam

class Verantwoordelijke(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)
	bezoekadres = models.TextField()
	
	def __unicode__(self):
		return self.naam

class Doel(models.Model):
	melding = models.ForeignKey(Melding)
	naam = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.naam



