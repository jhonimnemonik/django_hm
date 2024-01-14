# Generated by Django 3.2.10 on 2024-01-07 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20231218_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='Минимальная длина имени - 3 символа'), django.core.validators.RegexValidator(code='invalid_name', message='Имя должно содержать только буквы.', regex='^[a-zA-Zа-яА-Я\\s]+$')], verbose_name='Имя'),
        ),
    ]