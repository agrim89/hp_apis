# Generated by Django 2.0.2 on 2018-02-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20180220_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='modified',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
