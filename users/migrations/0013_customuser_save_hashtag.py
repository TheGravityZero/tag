# Generated by Django 4.2.4 on 2023-09-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_customuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='save_hashtag',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Хештег пользователя'),
        ),
    ]
