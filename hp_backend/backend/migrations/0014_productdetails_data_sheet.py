# Generated by Django 2.0 on 2018-02-16 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20180216_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='data_sheet',
            field=models.URLField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
