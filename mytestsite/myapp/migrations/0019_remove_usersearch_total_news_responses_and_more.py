# Generated by Django 4.2.6 on 2023-10-10 13:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0018_rename_count_usersearch_total_news_responses_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersearch",
            name="total_news_responses",
        ),
        migrations.RemoveField(
            model_name="usersearch",
            name="total_reddit_responses",
        ),
    ]
