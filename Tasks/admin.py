from django.contrib import admin
from Tasks.models import Category, TodoList

# Register your models here.

admin.site.register(Category)
admin.site.register(TodoList)
