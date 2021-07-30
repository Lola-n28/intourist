from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.db.models.fields import CharField
from django.db.models.query import ValuesIterable
# 
class Place(models.Model):
    user = models.ForeignKey(
         to=User, on_delete=models.SET_NULL,
         null = True, blank = True    
    )
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)
    img = models.ImageField(upload_to='places', null=True, blank=True)

# метод отображения
    def __str__(self): 
        return self.name

# настройки класса
    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'
        ordering = ['name'] # сортировка по name

class Feedback(models.Model):
    # many to 1
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        verbose_name='Пользователь'  # отображение атрибута
    )

    place = models.ForeignKey(
        to=Place,  #  к модели Place
        on_delete=models.CASCADE,
        verbose_name='Место'
    )

    # текст обратной связи
    text = models.TextField(verbose_name='Текст обратной связи')

    checked = models.BooleanField(default=False, verbose_name='Обработано')

    def __str__(self):
        return self.text[:20] # текст до 20 символов

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'


