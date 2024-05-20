# Generated by Django 4.2.12 on 2024-05-15 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0035_alter_comment_created_date_alter_like_user_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookmark",
            options={"verbose_name": "BookMark"},
        ),
        migrations.RemoveField(
            model_name="bookmark",
            name="bookmarks",
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 15, 14, 57, 50, 600533)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 15, 14, 57, 50, 600533)
            ),
        ),
    ]