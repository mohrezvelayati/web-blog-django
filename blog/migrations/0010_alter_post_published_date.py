# Generated by Django 4.2.12 on 2024-05-13 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_like_like_alter_post_published_date_save"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 13, 11, 46, 41, 899292)
            ),
        ),
    ]