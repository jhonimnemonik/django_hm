from django.shortcuts import render, redirect
from loader.models import Pets
from loader.forms import PhotosForm


def photo_load(request):
    img_form = PhotosForm()
    if request.method == "POST":
        img_form = PhotosForm(request.POST, request.FILES)
        if img_form.is_valid():
            obj = img_form.save(commit=False)
            obj.save()
            return redirect("photo_load")
    return render(request, "photo.html", {"page": "photo", "form": img_form})


def pets(request):
    pets = Pets.objects.get(id=1)
    img = pets.photos.all()
    data_from_db = Pets.objects.all()
    return render(request, "pets.html", {"data_from_db": data_from_db, "images": img})

#
# from django.shortcuts import render, redirect
# from .forms import PetsForm, PhotosForm
#
#
# def add_pet(request):
#     if request.method == "POST":
#         pet_form = PetsForm(request.POST)
#         photo_form = PhotosForm(request.POST, request.FILES)
#         if pet_form.is_valid() and photo_form.is_valid():
#             pet_instance = pet_form.save()
#             photo_form.instance.pets = pet_instance
#             photo_form.save()
#             return redirect("pets")
#     else:
#         pet_form = PetsForm()
#         photo_form = PhotosForm()
#     return render(request, "photo.html", {"pet_form": pet_form, "photo_form": photo_form})
