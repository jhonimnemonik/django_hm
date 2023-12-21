from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator


class Message(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Имя",
        validators=[
            MinLengthValidator(
                limit_value=3,
                message="Минимальная длина имени - 3 символа"
            ),
            RegexValidator(
                regex='^[a-zA-Zа-яА-Я]+$',
                message='Имя должно содержать только буквы.',
                code='invalid_name'
            )
        ]
    )
    email = models.EmailField(verbose_name="Почта")
    subject = models.CharField(max_length=50, verbose_name="Тема")
    message = models.TextField(max_length=150)
    date = models.DateTimeField(default=timezone.now, editable=False)
    is_processed = models.BooleanField(default=False)

    class Meta:
        db_table = "messages"
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
    #
    # def __str__(self):
    #     return self.name
