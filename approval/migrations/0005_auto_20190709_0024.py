# Generated by Django 2.2.3 on 2019-07-08 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0004_auto_20190709_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='approval.UserGroup'),
        ),
    ]
