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
	inlines = [MeldingInline]

admin.site.register(Company, CompanyAdmin)

class MeldingAdmin(admin.ModelAdmin):
	list_display = ("naam", "description", "doorgifte_passend", "doorgifte_buiten_eu")
	list_filter = ("doorgifte_passend", "doorgifte_buiten_eu")
	inlines = [BetrokkeneInline, DoelInline, OntvangerInline]
admin.site.register(Melding, MeldingAdmin)

class BetrokkeneAdmin(admin.ModelAdmin):
	list_display = ("naam",)
	search_fields = ("naam",)
	inlines = [BetrokkeneDetailsInline,]

admin.site.register(Betrokkene, BetrokkeneAdmin)

class BetrokkeneDetailsAdmin(admin.ModelAdmin):
	list_display = ("naam", "omschrijving")

admin.site.register(BetrokkeneDetails, BetrokkeneDetailsAdmin)



