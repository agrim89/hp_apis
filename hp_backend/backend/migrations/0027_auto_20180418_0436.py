# Generated by Django 2.0 on 2018-04-18 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_product_desciption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desciption',
            new_name='description',
        ),
    ]
