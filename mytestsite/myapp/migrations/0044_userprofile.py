# Generated by Django 4.2.6 on 2023-10-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0043_alter_usersearch_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("u_name", models.CharField(max_length=30)),
                ("u_email", models.CharField(max_length=30)),
            ],
        ),
    ]
