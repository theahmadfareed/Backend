# Generated by Django 4.2.6 on 2023-10-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0038_remove_news_articles_k1_keyword_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersearch",
            name="graph_data",
            field=models.JSONField(default=None, null=True),
        ),
    ]