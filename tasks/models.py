from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    due_date = models.DateTimeField('Срок выполнения', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']