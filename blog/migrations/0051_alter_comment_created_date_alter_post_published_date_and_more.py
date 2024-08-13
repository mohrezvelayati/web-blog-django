# Generated by Django 5.0.6 on 2024-08-11 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_alter_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 10, 26, 42, 746677)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 10, 26, 42, 746677)),
        ),
        migrations.DeleteModel(
            name='CommentReply',
        ),
    ]