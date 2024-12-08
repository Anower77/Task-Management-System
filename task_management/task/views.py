from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

# Add
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/task/show/')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})


# Show
def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_task.html', {'tasks': tasks})


# Edit
def edit_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/task/show/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/add_task.html', {'form': form})




# Delete 
def delete_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.delete()
    return redirect('/task/show/')



# Complete
def complete_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect('/task/show/')
