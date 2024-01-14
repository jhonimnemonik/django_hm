import os
import uuid
from pathlib import Path

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_save
from PIL import Image

import logging

logger = logging.getLogger(__name__)


class TypePet(models.TextChoices):
    CAT = "C", "Кошка"
    DOG = "D", "Собака"
    RODENTS = "R", "Грызун"
    BIRDS = "B", "Птица"
    REPTILES = "RT", "Рептилия"
    INSECTS = "I", "Насекомое"


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
    type_pet = models.CharField(max_length=2, choices=TypePet.choices, verbose_name="Вид животного")
    birth_date = models.DateField(verbose_name="Дата рождения")
    breed = models.CharField(max_length=25, default=None, verbose_name="Порода")
    is_male = models.BooleanField(default=True, verbose_name="Самец")
    description = models.TextField(max_length=150)
    nursery = models.ForeignKey(
        Nursery, null=True, on_delete=models.SET_NULL, blank=True, related_name="pets", verbose_name="Питомник"
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
        date = utc_time.strftime("%d%m%Y")
        file_name = uuid.uuid4().hex[:6]
        return f"{path}/{date}_{file_name}{ext}"

    img = models.ImageField(upload_to=_load_to)
    preview = models.ImageField(blank=True)
    middle = models.ImageField(blank=True)
    pets = models.ForeignKey(Pets, on_delete=models.SET_NULL, null=True, related_name="photos")
    priority = models.SmallIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pets.name} - {self.img}"

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


def preview_resize(path: Path, prev_path: Path):
    img = Image.open(path)
    small_img = img.resize((150, 100), 2)
    small_img.save(prev_path)


def middle_resize(path: Path, prev_path: Path):
    img = Image.open(path)
    original_width, original_height = img.size
    new_width = original_width // 2
    new_height = original_height // 2
    middle_img = img.resize((new_width, new_height), 3)
    middle_img.save(prev_path)


@receiver(post_save, sender=Photos)
def generate_resized_images(sender, instance, created, **kwargs):
    if created:
        try:
            old_instance = sender.objects.get(id=instance.id)
        except sender.DoesNotExist:
            return
        if instance.img.path == old_instance.img.path:
            original_file_path = Path(instance.img.path)
            media_root = Path(settings.MEDIA_ROOT)
            parent_directory = original_file_path.parent.parent

            preview_dir = parent_directory / "preview"
            preview_dir.mkdir(parents=True, exist_ok=True)
            file_name = original_file_path.name
            preview_path = preview_dir / file_name
            preview_resize(original_file_path, preview_path)
            instance.preview.name = str(preview_path.relative_to(media_root))

            middle_dir = parent_directory / "middle"
            middle_dir.mkdir(parents=True, exist_ok=True)
            middle_path = middle_dir / file_name
            middle_resize(original_file_path, middle_path)
            logger.info(f"Middle image saved at: {middle_path}")
            instance.middle.name = str(middle_path.relative_to(media_root))

            instance.save()
