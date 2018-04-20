# Generated by Django 2.0 on 2018-04-20 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_auto_20180418_0436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ram',
            new_name='memory',
        ),
        migrations.AddField(
            model_name='product',
            name='expansion_slots',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='network_interface',
            field=models.CharField(default="none", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ports',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.CharField(default="none", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(default="none", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='operating_system',
            field=models.CharField(default="none", max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='part_no',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='screen_size',
            field=models.CharField(default="none", max_length=1000),
            preserve_default=False,
        ),
    ]
