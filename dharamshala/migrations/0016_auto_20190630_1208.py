# Generated by Django 2.2.2 on 2019-06-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0015_auto_20190629_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shala',
            name='name_with_space',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='shala',
            name='name_without_space',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]