# Generated by Django 2.0 on 2018-02-20 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20180220_0541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['-company_name'], 'verbose_name_plural': 'Partner'},
        ),
        migrations.AlterModelOptions(
            name='partnersalesteam',
            options={'ordering': ('email',), 'verbose_name_plural': 'PartnerSalesTeam'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category',), 'verbose_name_plural': 'Product'},
        ),
    ]