# Generated by Django 4.2.6 on 2023-10-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0012_remove_redditarticle_k1_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsarticle_k1",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name="newsarticle_k2",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name="newsarticle_k3",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name="redditarticle_k1",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name="redditarticle_k2",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name="redditarticle_k3",
            name="sentiments",
            field=models.JSONField(default=None),
        ),
    ]