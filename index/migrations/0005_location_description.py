# Generated by Django 4.2.4 on 2023-09-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default=1, max_length=500, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]