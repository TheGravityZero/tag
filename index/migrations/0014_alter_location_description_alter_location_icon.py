# Generated by Django 4.2.4 on 2023-10-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/', verbose_name='Иконка'),
        ),
    ]
