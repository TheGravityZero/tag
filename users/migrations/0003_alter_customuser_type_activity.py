# Generated by Django 4.2.4 on 2023-09-22 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_typeactivity_customuser_birthday_wishlist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.typeactivity', verbose_name='Род деятельности'),
        ),
    ]
