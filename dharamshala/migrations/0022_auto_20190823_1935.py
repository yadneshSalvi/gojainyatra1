# Generated by Django 2.2.2 on 2019-08-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0021_auto_20190823_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='email_of_dharamshala_or_bunglow_or_sanatorium',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
    ]