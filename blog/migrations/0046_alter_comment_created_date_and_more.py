# Generated by Django 5.0.6 on 2024-08-06 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_alter_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 13, 55, 12, 786452)),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 13, 55, 12, 786452)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 13, 55, 12, 785444)),
        ),
    ]
