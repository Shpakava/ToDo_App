from django.urls import path
from Tasks.views import todo, category, redirect_view, add_task


app_name = 'Tasks'

urlpatterns = [
    path('', redirect_view),
    path('todo/', todo, name="TodoList"),
    path('category/', category, name="Category"),
    path("add/", add_task, name="add_task")
]
