# Generated by Django 4.2.6 on 2023-10-11 22:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0023_usersearch_total_news_responses_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersearch",
            old_name="keyword_total_sentiments",
            new_name="each_keyword_total_sentiments",
        ),
    ]
