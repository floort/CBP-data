import glob
import json

import django
from django.core.management import setup_environ
import settings
from register.models import *
setup_environ(settings)

for f in glob.glob("/home/floort/devel/pim/data/*.json"):
	print f
	companies = json.load(open(f))
	for c in companies:
		comp = Company()
		comp.url = c["url"]
		comp.name = c["name"]
		try:
			comp.save()
		except django.db.utils.IntegrityError:
			comp = Company.objects.get(url=c["url"])
		for mid in c["meldingen"].keys():
			m = c["meldingen"][mid]
			melding = Melding()
			melding.cbpid = mid
			melding.company = comp
			melding.description = m["description"]
			if m["doorgifte_passend"] == "J":
				melding.doorgifte_passend = "Y"
			elif m["doorgifte_passend"] == "N":
				melding.doorgifte_passend = "N"
			else:
				melding.doorgifte_passend = "?"
			melding.url = m["url"]
			melding.doorgifte_buiten_eu = m["doorgifte_buiten_eu"]
			melding.naam = m["naam_verwerking"]
			melding.save()
			if m.has_key("betrokkenen"):
				for betr in m["betrokkenen"].keys():
					b = Betrokkene()
					b.naam = betr
					b.melding = melding
					b.save()
					for detail in m["betrokkenen"][betr].keys():
						bd = BetrokkeneDetails()
						bd.naam = detail
						bd.omschrijving =  m["betrokkenen"][betr][detail]
						bd.betrokkene = b
						bd.save()
					b.save()
			if m.has_key("ontvangers"):
				for ontv in m["ontvangers"]:
					o = Ontvanger(naam=ontv)
					o.melding = melding
					o.save()
			if m.has_key("verantwoordelijken"):
				for verant in m["verantwoordelijken"]:
					v = Verantwoordelijke()
					v.naam = verant["Naam"]
					v.bezoekadres = verant["Bezoekadres"]
					v.melding = melding
					v.save()
			if m.has_key("doelen"):
				for doel in m["doelen"]:
					d = Doel(naam=doel)
					d.melding = melding
					d.save()
			#melding.save()
			#comp.meldingen.add(melding)
		comp.save()

			



