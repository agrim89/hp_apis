# Generated by Django 2.0 on 2018-03-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20180323_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usertype',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]