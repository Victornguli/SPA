# Generated by Django 2.2.3 on 2019-07-12 03:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0010_auto_20190711_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='add_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2019, 7, 12, 3, 32, 57, 769374, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
