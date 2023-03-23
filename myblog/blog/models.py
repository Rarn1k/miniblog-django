from django.db import models


class Post(models.Model):
    """Данные о посте"""
    title = models.CharField(verbose_name='Заголовок записи', max_length=150)
    description = models.TextField(verbose_name='Текст записи')
    author = models.CharField(verbose_name='Имя автора', max_length=150)
    date = models.DateField(verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

