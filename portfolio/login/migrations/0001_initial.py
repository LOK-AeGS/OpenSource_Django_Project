# Generated by Django 5.2 on 2025-05-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminUser",
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
                ("userName", models.CharField(max_length=10)),
                ("userId", models.CharField(max_length=10)),
                ("userPassword", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("userName", models.CharField(max_length=10)),
                ("userId", models.CharField(max_length=10)),
                ("userPassword", models.CharField(max_length=10)),
            ],
        ),
    ]
