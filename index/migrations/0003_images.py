# Generated by Django 4.2.4 on 2023-09-22 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_hashtag_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='location_img/')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.location')),
            ],
        ),
    ]
