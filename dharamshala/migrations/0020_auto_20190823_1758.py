# Generated by Django 2.2.2 on 2019-08-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0019_auto_20190817_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='check_in_time_given_by_dharamshala',
            field=models.CharField(blank=True, default='-', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='check_in_time_given_by_yatri',
            field=models.CharField(blank=True, default='-', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='check_out_time_given_by_dharamshala',
            field=models.CharField(blank=True, default='-', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='check_out_time_given_by_yatri',
            field=models.CharField(blank=True, default='-', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='email_of_dharamshala_or_bunglow_or_sanatorium',
            field=models.EmailField(blank=True, default='-', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='gojainyatra_email_id',
            field=models.CharField(blank=True, default='-', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='gojainyatra_phone_no',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='voucher',
            name='service_charge',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='phone_of_dharamshala_or_bunglow_or_sanatorium',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
