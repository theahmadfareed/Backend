# Generated by Django 4.2.6 on 2023-10-12 13:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0025_reddit_comments_news_articles"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news_articles",
            name="K1_news_sentiments",
        ),
        migrations.RemoveField(
            model_name="news_articles",
            name="K2_news_sentiments",
        ),
        migrations.RemoveField(
            model_name="news_articles",
            name="K3_news_sentiments",
        ),
        migrations.RemoveField(
            model_name="news_articles",
            name="each_keyword_news_sentiments",
        ),
        migrations.RemoveField(
            model_name="news_articles",
            name="news_total_sentiments",
        ),
        migrations.RemoveField(
            model_name="reddit_comments",
            name="K1_reddit_sentiments",
        ),
        migrations.RemoveField(
            model_name="reddit_comments",
            name="K2_reddit_sentiments",
        ),
        migrations.RemoveField(
            model_name="reddit_comments",
            name="K3_reddit_sentiments",
        ),
        migrations.RemoveField(
            model_name="reddit_comments",
            name="each_keyword_reddit_sentiments",
        ),
        migrations.RemoveField(
            model_name="reddit_comments",
            name="reddit_total_sentiments",
        ),
    ]