# Generated by Django 4.2.4 on 2023-09-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_created_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='extension',
            field=models.BooleanField(blank=True, null=True, verbose_name='Продление'),
        ),
    ]
