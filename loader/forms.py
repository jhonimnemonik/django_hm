from django import forms
from loader.models import Photos, Pets


class PhotosForm(forms.ModelForm):
    img = forms.ImageField(label="")
    pets = forms.ModelChoiceField(
        label="Выбор животного:", queryset=Pets.objects.all(), widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Photos
        fields = ("img", "pets")
        widgets = {"pets_id": forms.HiddenInput()}

#
# from django import forms
# from loader.models import Pets, Photos, Nursery
#
#
# class PetsForm(forms.ModelForm):
#     class Meta:
#         model = Pets
#         fields = ["name", "type_pet", "birth_date", "breed", "is_male", "description", "nursery"]
#
#     widgets = {"birth_date": forms.DateInput(attrs={"type": "date"})}
#
#
# class NurseryForm(forms.ModelForm):
#     class Meta:
#         model = Nursery
#         fields = ["name", "location", "phone"]
#
#

# class PhotosForm(forms.ModelForm):
#     current_pet = forms.ModelChoiceField(
#         queryset=Pets.objects.all(),
#         widget=forms.HiddenInput(),
#         required=False,
#     )
#
#     class Meta:
#         model = Photos
#         fields = ["img", "current_pet", "priority", "is_main"]
#         widgets = {"priority": forms.NumberInput(attrs={"min": 0})}
#
#     def __init__(self, *args, **kwargs):
#         instance = kwargs.pop('instance', None)
#         super().__init__(*args, **kwargs)
#
#         if instance:
#             self.fields['current_pet'].initial = instance.pets
#
#     def save(self, commit=True):
#         self.instance.pets = self.cleaned_data['current_pet']
#         return super().save(commit)
