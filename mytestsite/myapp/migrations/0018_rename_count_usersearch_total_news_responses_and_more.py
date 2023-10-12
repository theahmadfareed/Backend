# Generated by Django 4.2.6 on 2023-10-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0017_usersearch_count"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersearch",
            old_name="count",
            new_name="total_news_responses",
        ),
        migrations.AddField(
            model_name="usersearch",
            name="total_reddit_responses",
            field=models.JSONField(default=None, null=True),
        ),
    ]