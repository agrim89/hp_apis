# Generated by Django 2.0 on 2018-02-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20180207_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=1000)),
                ('part_no', models.CharField(max_length=1000)),
                ('specification_details', models.CharField(max_length=1000)),
                ('processor', models.CharField(max_length=1000)),
                ('screen_size', models.CharField(max_length=1000)),
                ('warranty', models.CharField(max_length=1000)),
                ('ram', models.CharField(max_length=1000)),
                ('hard_disk', models.CharField(max_length=1000)),
                ('operating_system', models.CharField(max_length=1000)),
                ('screen', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=1000)),
                ('part_no', models.CharField(max_length=1000)),
                ('specification_details', models.CharField(max_length=1000)),
                ('processor', models.CharField(max_length=1000)),
                ('screen_size', models.CharField(max_length=1000)),
                ('warranty', models.CharField(max_length=1000)),
                ('ram', models.CharField(max_length=1000)),
                ('hard_disk', models.CharField(max_length=1000)),
                ('operating_system', models.CharField(max_length=1000)),
                ('screen', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=1000)),
                ('part_no', models.CharField(max_length=1000)),
                ('specification_details', models.CharField(max_length=1000)),
                ('processor', models.CharField(max_length=1000)),
                ('graphics', models.CharField(max_length=1000)),
                ('warranty', models.CharField(max_length=1000)),
                ('ram', models.CharField(max_length=1000)),
                ('hard_disk', models.CharField(max_length=1000)),
                ('odd', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=1000)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
        ),
    ]
