# Generated by Django 5.0.6 on 2024-08-05 12:40

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_post_slug_alter_comment_created_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 16, 10, 54, 513581)),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 16, 10, 54, 513581)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 16, 10, 54, 513581)),
        ),
    ]