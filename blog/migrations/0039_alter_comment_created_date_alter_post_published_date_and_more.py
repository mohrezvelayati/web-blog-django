# Generated by Django 5.0.6 on 2024-05-20 10:43

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_alter_comment_created_date_alter_post_published_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 14, 13, 45, 232008)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 14, 13, 45, 228992)),
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('approved', models.BooleanField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 5, 20, 14, 13, 45, 232008))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
        ),
    ]