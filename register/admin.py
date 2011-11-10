from register.models import *
from django.contrib import admin

class MeldingInline(admin.TabularInline):
	model = Company.meldingen.through
	extra = 1
	#fields = ["url"]

class DoelInline(admin.TabularInline):
	model = Doel
	extra = 1
	fields = ["naam"]

class OntvangerInline(admin.TabularInline):
	model = Ontvanger
	extra = 1
	fields = ["naam"]

class BetrokkeneInline(admin.TabularInline):
	model = Betrokkene
	extra = 1
	fields = ["naam"]

class VerantwoordelijkeInline(admin.TabularInline):
	model = Verantwoordelijke
	extra = 1
	fields = ["naam", "bezoekadres"]

class BetrokkeneDetailsInline(admin.TabularInline):
	model = BetrokkeneDetails
	extra = 1
	fields = ["naam", "omschrijving"]

class CompanyAdmin(admin.ModelAdmin):
	list_display = ("name", "link")
	fieldsets = (
		(None, {
			"fields": ("name", "url")
		}),
	)
	search_fields = ("name", "meldingen__naam", "meldingen__description")
	inlines = [MeldingInline]

admin.site.register(Company, CompanyAdmin)

class MeldingAdmin(admin.ModelAdmin):
	list_display = ("cbpid", "naam", "description", "doorgifte_passend", "doorgifte_buiten_eu", "link")
	list_filter = ("doorgifte_passend", "doorgifte_buiten_eu")
	search_fields = ("naam", "description", "id")
	inlines = [
		BetrokkeneInline, 
		DoelInline, 
		OntvangerInline,
		VerantwoordelijkeInline,
	]
admin.site.register(Melding, MeldingAdmin)

class BetrokkeneAdmin(admin.ModelAdmin):
	list_display = ("melding", "naam")
	search_fields = ("naam",)
	inlines = [BetrokkeneDetailsInline,]

admin.site.register(Betrokkene, BetrokkeneAdmin)

class BetrokkeneDetailsAdmin(admin.ModelAdmin):
	list_display = ("naam", "omschrijving")

admin.site.register(BetrokkeneDetails, BetrokkeneDetailsAdmin)



