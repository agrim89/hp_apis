# Generated by Django 2.0.2 on 2018-02-09 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20180209_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspc',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 474722)),
        ),
        migrations.AlterField(
            model_name='businesspc',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 474752)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 475443)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 475467)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 476115)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 26, 11, 476138)),
        ),
    ]
