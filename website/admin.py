from django.contrib import admin
from . import models

# Register your models here.




@admin.register(models.Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ["email", "date_add", "date_update", "status"]
    list_editable = ('status',)



@admin.register(models.configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["description_newsletters", "date_add", "date_update", "status"]
    list_editable = ('status',)


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ["nom_site", "date_add", "date_update", "status"]
    list_editable = ('status',)


@admin.register(models.Lien_sociaux)
class Lien_sociauxAdmin(admin.ModelAdmin):
    list_display = ["nom", "icone", "liens", "date_add", "date_update", "status"]
    list_editable = ('status',)