# Generated by Django 5.0.6 on 2024-05-14 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_like_user_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 12, 49, 0, 522649)),
        ),
    ]