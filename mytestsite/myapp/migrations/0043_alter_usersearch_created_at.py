# Generated by Django 4.2.6 on 2023-10-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0042_alter_usersearch_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersearch",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
