from copy import copy
from register.models import *
from django.contrib import admin

class MeldingInline(admin.TabularInline):
    model = Melding
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
    list_display = ("name", "tags_str", "link")
    list_filter = ['tags', ]
    fieldsets = (
        (None, {
            "fields": ("name", "url", "tags")
        }),
    )
    search_fields = ("name", "melding__naam", "melding__description", )
    inlines = [MeldingInline]

    def get_actions(self, request):
        actions = super(CompanyAdmin, self).get_actions(request)
        for tag in Tag.objects.all():
            tag = unicode(tag.name)
            def a(modeladmin, request, queryset, tag=tag):
                for company in queryset:
                    tag = Tag.objects.get(name=tag)
                    company.tags.add(tag)
                    company.save()
            actions["add_tag_%s" % (tag)] = (
                copy(a), "add_tag_%s" % (tag), "Add tag %s" % (tag))
            def d(modeladmin, request, queryset, tag=tag):
                for company in queryset:
                    tag = Tag.objects.get(name=tag)
                    company.tags.remove(tag)
                    company.save()
            actions["del_tag_%s" % (tag)] = (
                copy(d), "del_tag_%s" % (tag), "Remove tag %s" % (tag))
        return actions


admin.site.register(Company, CompanyAdmin)

class MeldingAdmin(admin.ModelAdmin):
	list_display = ("cbpid", "naam", "description", "company",
        "doorgifte_passend", "doorgifte_buiten_eu", "link")
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

admin.site.register(Tag)

