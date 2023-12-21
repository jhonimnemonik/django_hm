from django.db import models


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
    photo = models.ImageField()
    description = models.TextField(max_length=150)
    nursery = models.ForeignKey(
        Nursery,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name="pets",
        verbose_name="Питомник"
    )

    class Meta:
        db_table = "pets"
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class Photos(models.Model):
    img = models.ImageField()
    preview = models.ImageField(blank=True)
    middle = models.ImageField(blank=True)
    pets_id = models.ForeignKey(
        Pets,
        on_delete=models.SET_NULL,
        null=True,
        related_name="photos"
    )
    priority = models.SmallIntegerField(default=0)
    data = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "ФотоГрафии"
