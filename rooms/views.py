from urllib.parse import urlencode
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    FormView,
)
from rooms.forms import CreatePhotoForm, CreateRoomForm
from rooms.models import Room, Photo, RoomType
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, reverse








# -------------------------- ROOMS -------------------#

# CREATE
class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    form_class = CreateRoomForm
    template_name = "room_create.html"
    success_url = reverse_lazy("rooms:host-list")
    

    def form_valid(self, form):
        form.instance.host = self.request.user.client
        print("success")
        return super(RoomCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RoomCreateView, self).get_context_data(**kwargs)
        return context
    

# LIST
class RoomHostListView(ListView):
    model = Room
    context_object_name = "rooms"
    template_name = "room_list.html"
    

    def get_queryset(self):
        return Room.objects.filter(host=self.request.user.client).order_by(
            "-created"
        )

    def get_context_data(self, **kwargs):
        context = super(RoomHostListView, self).get_context_data(**kwargs)
        
        # Add the total_rooms count to the context
        context["total_rooms"] = Room.objects.filter(host=self.request.user.client).count()
        return context
    
    
class RoomListView(ListView):
    model = Room
    paginate_by = 30
    context_object_name = "rooms"
    template_name = "listing.html"
    

    def get_queryset(self):
        return Room.objects.all().order_by("-created")

    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        return context



def room_category(request, slug):
    category = RoomType.objects.get(slug=slug)
    room = Room.objects.filter(room_type=category)


    return render(request, "room_category.html", locals())



# DETAIL
class RoomDetailView(DetailView):
    model = Room
    context_object_name = "room"
    template_name = "room_detail.html"

    


def book_room(request, pk):
    room_url = request.build_absolute_uri(reverse('rooms:detail', kwargs={'pk': pk}))
    message = f"Salut, je suis intéressé par cet appartement: {room_url}"
    
    # Define the recipient number
    recipient_number = '22890667515'  # Replace with the recipient's phone number
    
    # Construct the WhatsApp URL with recipient number and message
    whatsapp_params = {
        'text': message,
        'phone': recipient_number
    }
    whatsapp_url = f"https://api.whatsapp.com/send?{urlencode(whatsapp_params)}"
    
    return redirect(whatsapp_url)


# UPDATE
class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    form_class = CreateRoomForm
    template_name = "room_edit.html"
    success_url = reverse_lazy("rooms:host-list")
    

    def get_context_data(self, **kwargs):
        context = super(RoomUpdateView, self).get_context_data(**kwargs)
        return context
    

# DELETE
class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    success_url = reverse_lazy("rooms:host-list")
    template_name = "room_confirm_delete.html"

# -------------------------- ROOMS PHTOS -------------------#


class RoomPhotosView(LoginRequiredMixin, DetailView):

    model = Room
    template_name = "room_photo_list.html"

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.client.pk:
            raise Http404()
        return room


def delete_photo(request, room_pk, photo_pk):
    user = request.user.client
    try:
        room = Room.objects.get(pk=room_pk)
        if room.host.pk != user.pk:
            messages.error(request, "Can't delete that photo")
        else:
            Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo deleted")
        return redirect(reverse("rooms:photo-list", kwargs={"pk": room_pk}))
    except Room.DoesNotExist:
        return redirect(reverse("main:home"))


class EditPhotoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Photo
    template_name = "room_photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        room_pk = self.kwargs.get("room_pk")
        return reverse("rooms:photo-list", kwargs={"pk": room_pk})


class AddPhotoView(LoginRequiredMixin, FormView):

    template_name = "room_photo_create.html"
    fields = ("caption", "file")
    form_class = CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("rooms:photo-list", kwargs={"pk": pk}))





