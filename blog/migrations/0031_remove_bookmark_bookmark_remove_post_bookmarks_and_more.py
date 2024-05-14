# Generated by Django 5.0.6 on 2024-05-14 19:29

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_bookmark_bookmark_alter_comment_created_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='bookmark',
        ),
        migrations.RemoveField(
            model_name='post',
            name='bookmarks',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 22, 59, 26, 659154)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 22, 59, 26, 659154)),
        ),
    ]
