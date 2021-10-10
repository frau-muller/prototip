from django.db import models

class Question(models.Model):

    CHOICES_ANSWER = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    question = models.TextField(verbose_name="Вопрос")
    option_a = models.CharField(max_length=250, verbose_name="Выбор A")
    option_b = models.CharField(max_length=250, verbose_name="Выбор B")
    option_c = models.CharField(max_length=250, verbose_name="Выбор C")
    option_d = models.CharField(max_length=250, verbose_name="Выбор D")
    correct_answer = models.CharField(max_length=5, choices=CHOICES_ANSWER, verbose_name="Правильный ответ")
