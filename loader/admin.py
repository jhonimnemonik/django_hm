from django.contrib import admin
from loader.models import Pets, Nursery, Photos


@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ("name", "nursery", "type_pet", "birth_date", "breed", "is_male", "description")
    search_fields = ["name", "breed", "nursery__name"]
    list_filter = ["type_pet", "is_male", "nursery__name"]


admin.site.register(Nursery)
admin.site.register(Photos)
