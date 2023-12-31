# Generated by Django 4.2.6 on 2023-10-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0031_reddit_comments_k1_reddit_sentiments_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersearch",
            old_name="sentiments_from_news",
            new_name="each_keyword_sentiments_from_news",
        ),
        migrations.AddField(
            model_name="usersearch",
            name="each_keyword_sentiments_from_reddit",
            field=models.JSONField(default=None, null=True),
        ),
    ]
