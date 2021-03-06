# Generated by Django 2.0.2 on 2018-02-09 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180208_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspc',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 7, 4, 56, 820393)),
        ),
        migrations.AlterField(
            model_name='businesspc',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2018, 2, 9)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='created',
            field=models.DateTimeField(default=datetime.date(2018, 2, 9)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2018, 2, 9)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='created',
            field=models.DateTimeField(default=datetime.date(2018, 2, 9)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2018, 2, 9)),
        ),
    ]
