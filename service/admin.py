from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["images_view","prix","nom","categorie","marques", "description", "stock", "quantite", "date_add", "date_update", "status"]
    list_editable = ('status',)

    def images_view(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')
        return '-'

    images_view.short_description = 'Aperçu des images'



@admin.register(models.Categorie_articles)
class Categorie_articlesAdmin(admin.ModelAdmin):
    list_display = ["nom", "date_add", "date_update", "status"]
    list_editable = ('status',)



@admin.register(models.Marques_articles)
class Marques_articlesAdmin(admin.ModelAdmin):
    list_display = ["nom", "date_add", "date_update", "status"]
    list_editable = ('status',)


@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "company", "email", "pays", "adresse", "ville", "phone", "code_postal", "commentaire", "date_add", "date_update", "status"]
    list_editable = ('status',)


