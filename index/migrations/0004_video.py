# Generated by Django 4.2.4 on 2023-09-22 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='location_video/')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.location')),
            ],
        ),
    ]
