# Generated by Django 2.2.3 on 2019-07-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0006_auto_20190710_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
