# Generated by Django 2.0 on 2018-02-08 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20180208_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspc',
            name='created',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
        migrations.AlterField(
            model_name='businesspc',
            name='modified',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='created',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modified',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='created',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='modified',
            field=models.DateField(default=datetime.date(2018, 2, 8)),
        ),
    ]