from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Task Management System</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),  
    path('category/', include('category.urls')),  
    path('', home), 
]
