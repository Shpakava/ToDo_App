from django.shortcuts import render, redirect
from django.http import request
from .models import TodoList, Category
from .forms import AddTaskForm

# Create your views here.

def redirect_view(request):
    """Домашняя страница"""
    return redirect("/add")


def todo(request):
    """Функция удаления задачи"""
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
       if "Delete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox")
            for i in range(len(checkedlist)):
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete()
    return render(request, "todo.html", {"todos": todos, "categories": categories})


def category(request):
    """Функция добавления и удаления категорий"""
    categories = Category.objects.all()
    if request.method == "POST":
        if "Add" in request.POST:
            name = request.POST["name"]
            category = Category(name=name)
            category.save()
            return redirect("/category")
        if "Delete" in request.POST:
            check = request.POST.getlist("check")
            for i in range(len(check)):
                сateg = Category.objects.filter(id=int(check[i]))
                сateg.delete()
    return render(request, "category.html", {"categories": categories})


def add_task(request):
    """Функция добавления задач"""
    add_form = AddTaskForm()
    if request.method == "POST":
        add_form = AddTaskForm(request.POST)
        if add_form.is_valid():
            todo_list = TodoList(
                title=add_form.cleaned_data["title"],
                content=add_form.cleaned_data["content"],
                due_date=add_form.cleaned_data["due_date"],
                category=add_form.cleaned_data["category"]
            )
            todo_list.save()
            return render(request, "created.html", context={"todo_list": todo_list})
    return render(request, "create.html", context={"form": add_form})