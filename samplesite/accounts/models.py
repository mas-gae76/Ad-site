from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Товар')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['name']

    def clean(self):
        errors = {}
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Значение цены не может быть отрицательным')
        if errors:
            raise ValidationError(errors)
