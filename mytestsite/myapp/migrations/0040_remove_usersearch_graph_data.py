# Generated by Django 4.2.6 on 2023-10-16 14:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0039_usersearch_graph_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersearch",
            name="graph_data",
        ),
    ]
