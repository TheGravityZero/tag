# Generated by Django 4.2.4 on 2023-10-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_customuser_save_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='attempts',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во попыток'),
        ),
    ]