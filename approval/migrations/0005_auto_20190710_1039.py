# Generated by Django 2.2.3 on 2019-07-10 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0004_auto_20190710_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_title',
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 10, 10, 38, 50, 455389)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 10, 10, 39, 4, 225954)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sub_office',
            field=models.CharField(default='Nairobi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='unit',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_category',
            field=models.CharField(max_length=50),
        ),
    ]