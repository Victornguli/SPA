# Generated by Django 2.2.3 on 2019-07-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0003_auto_20190710_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='unit_name',
            field=models.CharField(default='Nutrition', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='unit',
            field=models.CharField(default='Nutrition', max_length=50),
        ),
    ]
