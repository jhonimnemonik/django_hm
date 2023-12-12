from django.db import models

class Messages(models.Model):
    user_name = models.CharField(max_length=25, verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта")
    subject = models.CharField(max_length=50, verbose_name="Тема")
    message = models.TextField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"