# Generated by Django 5.2 on 2025-05-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="userId",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
