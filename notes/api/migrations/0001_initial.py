# Generated by Django 4.2 on 2023-04-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("body", models.TextField()),
                ("update", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]
