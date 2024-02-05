from django.contrib.auth.models import AbstractUser
from django.db import models

from index.models import Location


class TypeActivity(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Род деятельности'
        verbose_name_plural = 'Род деятельности'

# Create your models here.
class CustomUser(AbstractUser):
    city = models.CharField(max_length=100, verbose_name='Город', blank=True, null=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', blank=True, null=True)
    insta = models.CharField(max_length=100, verbose_name='Instagram', blank=True, null=True)
    type_activity = models.ForeignKey('TypeActivity', on_delete=models.CASCADE, verbose_name='Род деятельности', blank=True, null=True)
    status = models.CharField(max_length=100, verbose_name='Статус пользователя', blank=True, null=True, default='free')
    rebill_id = models.CharField(max_length=200, verbose_name='Rebill ID', blank=True, null=True)
    created_pay = models.DateTimeField(verbose_name='Дата окончания подписки', blank=True, null=True)
    extension = models.BooleanField(verbose_name='Продление', blank=True, null=True)
    save_hashtag = models.CharField(max_length=100, verbose_name='Хештег пользователя', blank=True, null=True)
    attempts = models.IntegerField(verbose_name='Кол-во попыток', blank=True, null=True, default=0)


    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'