from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        abstract = True


class Poll(BaseModel):
    question = models.TextField(max_length=500, verbose_name='Вопрос')
    users = models.ManyToManyField(get_user_model(), related_name="polls", verbose_name="Пользователи")

    def __str__(self):
        return f'{self.id}. {self.question}'

    class Meta:
        db_table = 'Polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        permissions = [
            ('take_survey', 'Может пройти опрос')
        ]


class Choice(models.Model):
    option = models.TextField(max_length=200, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll',
                             on_delete=models.CASCADE,
                             verbose_name='Опрос',
                             related_name='choices')

    def __str__(self):
        return f'{self.id}. {self.option}'

    class Meta:
        db_table = 'Choices'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answer(BaseModel):
    poll = models.ForeignKey('webapp.Poll',
                             on_delete=models.CASCADE,
                             verbose_name='Опрос',
                             related_name='answers')
    option = models.ForeignKey('webapp.Choice',
                               on_delete=models.CASCADE,
                               related_name='answers',
                               verbose_name='Вариант ответа')

    class Meta:
        db_table = 'Answers'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
