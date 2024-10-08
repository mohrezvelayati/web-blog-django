# Generated by Django 5.0.6 on 2024-05-14 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 13, 15, 8, 394649)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 13, 15, 8, 394649)),
        ),
    ]
