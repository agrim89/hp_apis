# Generated by Django 2.0.2 on 2018-02-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20180209_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspc',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notebook',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='workstation',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
