# Generated by Django 2.0.2 on 2018-02-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
