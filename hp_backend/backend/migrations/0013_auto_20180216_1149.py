# Generated by Django 2.0 on 2018-02-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_productdetails_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.IntegerField(),
        ),
    ]
