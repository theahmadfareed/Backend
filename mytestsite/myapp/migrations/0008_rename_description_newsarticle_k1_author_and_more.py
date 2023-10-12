# Generated by Django 4.2.6 on 2023-10-09 16:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_alter_newsarticle_k1_published_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsarticle_k1",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="newsarticle_k1",
            old_name="title",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="newsarticle_k2",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="newsarticle_k2",
            old_name="title",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="newsarticle_k3",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="newsarticle_k3",
            old_name="title",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="redditarticle_k1",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="redditarticle_k1",
            old_name="title",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="redditarticle_k2",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="redditarticle_k2",
            old_name="title",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="redditarticle_k3",
            old_name="description",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="redditarticle_k3",
            old_name="title",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k1",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k1",
            name="url",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k2",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k2",
            name="url",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k3",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="newsarticle_k3",
            name="url",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k1",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k1",
            name="url",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k2",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k2",
            name="url",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k3",
            name="published_at",
        ),
        migrations.RemoveField(
            model_name="redditarticle_k3",
            name="url",
        ),
    ]
