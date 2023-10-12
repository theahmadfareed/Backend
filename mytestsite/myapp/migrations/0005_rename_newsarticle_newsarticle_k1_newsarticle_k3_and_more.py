# Generated by Django 4.2.6 on 2023-10-08 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_newsarticle_description_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewsArticle",
            new_name="NewsArticle_K1",
        ),
        migrations.CreateModel(
            name="NewsArticle_K3",
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
                ("title", models.TextField(null=True)),
                ("description", models.TextField(null=True)),
                ("url", models.TextField(null=True)),
                ("published_at", models.DateTimeField()),
                (
                    "user_search",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.usersearch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsArticle_K2",
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
                ("title", models.TextField(null=True)),
                ("description", models.TextField(null=True)),
                ("url", models.TextField(null=True)),
                ("published_at", models.DateTimeField()),
                (
                    "user_search",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.usersearch",
                    ),
                ),
            ],
        ),
    ]