# Generated by Django 4.2.6 on 2023-10-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0028_alter_news_articles_k1_news_sentiments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news_articles",
            name="K1_news_sentiments",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="news_articles",
            name="K2_news_sentiments",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="news_articles",
            name="K3_news_sentiments",
            field=models.JSONField(default=None, null=True),
        ),
    ]
