# Generated by Django 4.1.4 on 2022-12-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student_info",
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
                ("roll", models.CharField(max_length=10)),
                ("full_name", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="profilePIC")),
                ("department", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=13)),
            ],
        ),
    ]
