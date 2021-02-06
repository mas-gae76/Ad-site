from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Board(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    image = models.ImageField(verbose_name='Изображение', null=True, upload_to='images')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = "Объявление"
        ordering = ['-published']

    def clean(self):
        errors = {}
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Значение цены не может быть отрицательным')
        if errors:
            raise ValidationError(errors)
