from django.utils import timezone
from django.db import models


# Create your models here.

class Category(models.Model):
    """Таблица категорий"""
    name = models.CharField(max_length=100)

    class Meta:
        """Имена объектов"""
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Отображение в интерфейсе"""
        return self.name


class TodoList(models.Model):
    """Таблица задач"""
    status_option = (
        ("to_do", "to_do"),
        ("in_progress", "in_progress"),
        ("done", "done")
    )
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.CharField(max_length=20, choices=status_option, default="to_do")
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)

    class Meta:
        """Сортировка"""
        ordering = ["-created"]

    def __str__(self):
        """Отображение в интерфейсе"""
        return self.title

    def update_status(self):
        """Изменение статуса задачи"""
        if self.status == "to_do":
            self.status = "in_progress"
        elif self.status == "in_progress":
            self.status = "done"
        self.save()
