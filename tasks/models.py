from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнено'),
        ('cancelled', 'Отменено'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField('Наименование', max_length=200)
    description = models.TextField('Примечание', blank=True, null=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    due_date = models.DateTimeField('Дата выполнения', blank=True, null=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'