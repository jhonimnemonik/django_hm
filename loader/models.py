import os
import uuid
from pathlib import Path

from django.db import models
from django.utils import timezone
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_save
from PIL import Image


class TypePet(models.TextChoices):
    CAT = 'C', 'Кошка'
    DOG = 'D', 'Собака'
    RODENTS = 'R', 'Грызун'
    BIRDS = 'B', 'Птица'
    REPTILES = 'RT', 'Рептилия'
    INSECTS = 'I', 'Насекомое'


class Nursery(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название питомника")
    location = models.CharField(max_length=100, verbose_name="Местоположение питомника")
    phone = models.CharField(max_length=21, verbose_name="Номер телефона")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "nurseries"
        verbose_name = "Питомник"
        verbose_name_plural = "Питомники"


class Pets(models.Model):
    name = models.CharField(max_length=25, verbose_name="Имя")
    type_pet = models.CharField(
        max_length=2,
        choices=TypePet.choices,
        verbose_name="Вид животного"
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    breed = models.CharField(max_length=25, default=None, verbose_name="Порода")
    is_male = models.BooleanField(default=True, verbose_name="Самец")
    description = models.TextField(max_length=150)
    nursery = models.ForeignKey(
        Nursery,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name="pets",
        verbose_name="Питомник"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pets"
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class Photos(models.Model):
    def _load_to(self, filename):
        _, ext = os.path.splitext(filename)
        utc_time = timezone.now()
        pets_name = self.pets.name
        pets_type = self.pets.get_type_pet_display()
        path = f"pets/{pets_type}/{pets_name}/full"
        date = utc_time.strftime("%Y%m")
        file_name = uuid.uuid4(3).hex
        return f"{path}/{date}_{file_name}{ext}"

    img = models.ImageField(upload_to=_load_to)
    preview = models.ImageField(blank=True)
    middle = models.ImageField(blank=True)
    pets = models.ForeignKey(
        Pets,
        on_delete=models.SET_NULL,
        null=True,
        related_name="photos"
    )
    priority = models.SmallIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pets.name} - {self.img}"

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


def resize(path: Path, prev_path: Path):
    img = Image.open(path)
    small_img = img.resize((150, 100),2)
    small_img.save(prev_path)



@receiver(post_save, sender=Photos)
def preview_gen(sender, instance, created, **kwargs):
    if not created:
        pass
    # if instance.id is not None:
    #     old_instance = sender.objects.get(id=instance.id)
    #     if instance.img.path != old_instance.img.path:
    #         resize(Path(instance.img.path))
    else:
        preview_path = Path(instance.img.path.replace("/full", "/preview"))
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        resize(Path(instance.img.path), preview_path)
