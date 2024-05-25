from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

   
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    prix_par_nuit = forms.IntegerField(required=False)
    prix_par_semaine = forms.IntegerField(required=False)
    prix_par_mois = forms.IntegerField(required=False)
    nombre_de_chambres = forms.IntegerField(required=False)
    nombre_de_lits = forms.IntegerField(required=False)
    nombre_de_douche = forms.IntegerField(required=False)
    agrement = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilités = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()


class CreateRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateRoomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "custom-form"
            visible.field.widget.attrs["placeholder"] = " "
        
    class Meta:
        model = models.Room
        fields = (
            "nom",
            "description",
            "prix_par_nuit",
            "prix_par_semaine",
            "prix_par_mois",
            "caution",
            "adresse",
            "nombre_de_lits",
            "nombre_de_chambres",
            "nombre_de_douche",
            "room_type",
            "agrement",
            "facilités",
            "reglements",
            "video",
        )
        labels = {
            "nom": "Titre",
            "description": "Description",
            "prix_par_nuit": "Prix par nuit (xof)",
            "prix_par_semaine": "Prix par semaine (xof)",
            "prix_par_mois": "Prix par mois (xof)",
            "caution":"Caution",
            "adresse": "Adresse",
            "agrement": "Commodités",
            "facilités": "Installations",
            "reglements": "règles de la maison",
            "nombre_de_lits": "Nombre de lits",
            "nombre_de_chambres": "chambres",
            "room_type": "Type",
            "video": "Vidéo de presentation",
            "nombre_de_douche": "Douches",

        }

    
