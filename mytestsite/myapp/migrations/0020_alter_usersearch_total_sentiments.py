# Generated by Django 4.2.6 on 2023-10-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0019_remove_usersearch_total_news_responses_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersearch",
            name="total_sentiments",
            field=models.JSONField(default=list, null=True),
        ),
    ]
