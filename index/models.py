from django.db import models

class Question(models.Model):

    answer_text = models.TextField(max_length=2000)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class People(models.Model):
    fio = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    video = models.FileField(upload_to='uploads/')
    url = models.CharField(max_length=1000)
    preview = models.ImageField(upload_to='preview/', verbose_name='Изображение', null=True, blank=True)

class Hashtag(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хештеги'
        verbose_name_plural = 'Хештеги'


class Location(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок', null=True, blank=True)
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок', null=True, blank=True, default=' ')
    icon = models.ImageField(upload_to='icon/', verbose_name='Иконка')
    hashtag = models.ManyToManyField('Hashtag', verbose_name="Хештеги", blank=True, null=True)
    addresses = models.CharField(max_length=200, verbose_name='Адрес')
    latitude = models.CharField(max_length=250, verbose_name='Широта')
    longitude = models.CharField(max_length=250, verbose_name='Долгота')
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    promo = models.CharField(max_length=250, verbose_name='Промокод', null=True, blank=True, default=' ')
    promo_description = models.CharField(max_length=250, verbose_name='Описание промокода', null=True, blank=True, default=' ')
    city = models.CharField(max_length=250, verbose_name='Город', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локации'
        verbose_name_plural = 'Локации'

class Images(models.Model):
    note = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='location_img/',null=True,blank=True)

class Video(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.FileField(upload_to='location_video/',null=True,blank=True)


class Promo(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок', null=True, blank=True)
    percent = models.FloatField(verbose_name='Процент скидки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'