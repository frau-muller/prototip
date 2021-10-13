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

class Score(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    time = models.TimeField(verbose_name="Время", auto_now=False, auto_now_add=False)
    score = models.IntegerField(verbose_name="Очки")
    fifty_fifty = models.BooleanField(verbose_name="50-50", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="День создания")


    def username(self):
        return self.user.username

    username.short_description = 'Пользователь'

    class Meta:
        ordering = ['score']
        verbose_name = 'Балл'
        verbose_name_plural = 'Баллы'

    def __str__(self):
        return str(self.score)


class Prize(models.Model):
    amount = models.IntegerField(verbose_name="Сумма", null=False, blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Приз'
        verbose_name_plural = 'Призы'

    def __str__(self):
        return str(self.amount)