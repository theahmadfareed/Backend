# Generated by Django 4.2.6 on 2023-10-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0044_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersearch",
            name="k1_news_graph_data",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="usersearch",
            name="k2_news_graph_data",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="usersearch",
            name="k3_news_graph_data",
            field=models.JSONField(default=None, null=True),
        ),
    ]
