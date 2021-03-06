# Generated by Django 2.0.2 on 2018-02-07 07:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dealer_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=1000)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('login_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('domain_name', models.CharField(max_length=1000)),
                ('partner_id', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('dedicated_person', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=10)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
