from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    """Просмотр списка дел"""
    tasks = Task.objects.filter(user=request.user)
    
    # Фильтрация по статусу
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    
    context = {
        'tasks': tasks,
        'status_filter': status_filter,
        'search_query': search_query,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
    """Создание нового дела"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f'Дело "{task.title}" успешно создано!')
            return redirect('tasks:list')
        else:
            messages.error(request, 'Ошибка при создании дела. Проверьте данные.')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Создать'})

@login_required
def task_detail(request, pk):
    """Просмотр деталей дела"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_update(request, pk):
    """Редактирование дела"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Дело "{task.title}" обновлено!')
            return redirect('tasks:list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'task': task,
        'action': 'Редактировать'
    })

@login_required
def task_delete(request, pk):
    """Удаление дела"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Дело "{task_title}" удалено!')
        return redirect('tasks:list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_complete(request, pk):
    """Отметить дело как выполненное"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = 'completed'
    task.save()
    messages.success(request, f'Дело "{task.title}" выполнено!')
    return redirect('tasks:list')