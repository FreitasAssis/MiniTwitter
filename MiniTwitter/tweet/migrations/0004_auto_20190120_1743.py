# Generated by Django 2.0.10 on 2019-01-20 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20190120_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
