# Generated by Django 4.2.1 on 2023-05-08 17:23

from django.db import migrations, models
import django.db.models.deletion
import projetoApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ToDoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "due_date",
                    models.DateTimeField(default=projetoApp.models.one_week_hence),
                ),
                (
                    "todo_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projetoApp.todolist",
                    ),
                ),
            ],
            options={
                "ordering": ["due_date"],
            },
        ),
    ]