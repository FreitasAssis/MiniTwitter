# Generated by Django 2.0.10 on 2019-01-20 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20190120_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 17, 43, 21, 285431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
