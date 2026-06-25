from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Введите примечание...'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите название дела...'}
            ),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Наименование',
            'description': 'Примечание',
            'due_date': 'Дата выполнения',
            'status': 'Статус',
        }