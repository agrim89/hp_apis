# Generated by Django 2.0 on 2018-02-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_businesspc_notebook_workstation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspc',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='businesspc',
            name='modified',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modified',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='modified',
            field=models.DateField(),
        ),
    ]