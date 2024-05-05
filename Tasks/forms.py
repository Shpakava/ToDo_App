from django import forms
from Tasks.models import TodoList


class AddTaskForm(forms.ModelForm):

    """Форма добавления задачи"""
    class Meta:
        model = TodoList
        fields = "__all__"
        exclude = ["created"]