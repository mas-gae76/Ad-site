from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .utilities import get_timestamp_path


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
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to=get_timestamp_path)
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    contacts = models.TextField(verbose_name='Контакты')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    edited = models.DateTimeField(auto_now=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    is_edited = models.BooleanField(default=False, db_index=True, verbose_name='Изменено')
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

    def delete(self, *args, **kwargs):
        for i in self.AdditionalImage_set.all():
            i.delete()
        super().delete(*args, **kwargs)


class AdditionalImage(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Объявление')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Дополнительные иллюстрации'
        verbose_name = 'Дополнительная иллюстрация'
