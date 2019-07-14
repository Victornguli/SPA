# Generated by Django 2.2.3 on 2019-07-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval', '0005_auto_20190710_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('tech', 'Technical_Review'), ('prc_review', 'PRC_Review'), ('prc_meeting', 'PRC_Meeting'), ('nfr', 'NFR_Created'), ('closed', 'Closed')], default='new', max_length=50),
        ),
    ]