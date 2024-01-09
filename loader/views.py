from django.shortcuts import render
from loader.models import Pets
from loader.forms import PhotosForm


def photo_load(request):
    # pets = Pets.objects.get(id=1)
    img_form = PhotosForm()
    if request.method == "POST":
        img_form = PhotosForm(request.POST, request.FILES)
        if img_form.is_valid():
            obj = img_form.save(commit=False)
            obj.save()
        # uploaded_file = request.FILES.get("file")
        # if uploaded_file:
        #     with open("loaded.png", "wb") as img_file:
        #         img_file.write(uploaded_file.read())
    return render(request, "photo.html", {"page": "photo", "form": img_form})

def pets(request):
    data_from_db = Pets.objects.all()
    return render(request, 'pets.html', {'data_from_db': data_from_db})


# from django.shortcuts import render, redirect
# from .models import Pets
# from .forms import PetsForm, PhotosForm
#
#
# def add_pet(request):
#     if request.method == 'POST':
#         pet_form = PetsForm(request.POST)
#         photo_form = PhotosForm(request.POST, request.FILES)
#         if pet_form.is_valid() and photo_form.is_valid():
#             pet = pet_form.save()
#             photo = photo_form.save(commit=False)
#             photo.pets = pet
#             photo.save()
#             return redirect('pets')
#     else:
#         pet_form = PetsForm()
#         photo_form = PhotosForm()
#     return render(request, 'photo.html', {'pet_form': pet_form, 'photo_form': photo_form})
#
#
# def pets(request):
#     data_from_db = Pets.objects.all()
#     return render(request, 'pets.html', {'data_from_db': data_from_db})

