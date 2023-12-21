from django.contrib import admin
from loader.models import Pets


class AddPetsAdmin(admin.ModelAdmin):
    fields = ("category", "cost")


admin.register(Pets, AddPetsAdmin)