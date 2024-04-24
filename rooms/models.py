from django.utils import timezone
from django.db import models
from django.urls import reverse
from main import models as main_models
from calendar import Calendar


class AbstractItem(main_models.TimeStampedModel):
    name = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class Reglement(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(main_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(main_models.TimeStampedModel):
    nom = models.CharField(max_length=140)
    description = models.TextField()
    prix_par_nuit = models.IntegerField()
    prix_par_mois = models.IntegerField()
    adresse = models.CharField(max_length=200)
    nombre_de_lits = models.IntegerField()
    nombre_de_chambres = models.IntegerField()
    nombre_de_douche = models.IntegerField()
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    agrement = models.ManyToManyField("Amenity", related_name="rooms", blank=True,)
    facilités = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    reglements = models.ManyToManyField("Reglement", related_name="rooms", blank=True)

    video = models.FileField(upload_to="room_videos", blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

   
