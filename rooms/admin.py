from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Reglement)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("nom", "room_type", "description", "adresse", "prix_par_nuit", "prix_par_mois")},
        ),
        ("Spaces", {"fields": ("nombre_de_lits", "nombre_de_chambres", "nombre_de_douche")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("agrement", "facilités", "reglements"),
            },
        ),
    )

    ordering = ("nom", "prix_par_nuit", "prix_par_mois", "nombre_de_chambres")

    list_display = (
        "nom",
        "prix_par_nuit",
        "prix_par_mois",
        "nombre_de_lits",
        "nombre_de_chambres",
        "nombre_de_douche",
        "count_amenities",
        "count_photos",
        # "total_rating",
    )

    list_filter = (
        "room_type",
        "agrement",
        "facilités",
        "reglements",
    )

    filter_horizontal = (
        "agrement",
        "facilités",
        "reglements",
    )


    def count_amenities(self, obj):
        return obj.agrement.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
