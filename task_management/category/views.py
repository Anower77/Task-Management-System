from django.shortcuts import render, redirect
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/task/add/')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})
