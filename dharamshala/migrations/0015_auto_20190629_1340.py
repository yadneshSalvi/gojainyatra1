# Generated by Django 2.2.2 on 2019-06-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dharamshala', '0014_shala_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shala',
            name='ranking',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterOrderWithRespectTo(
            name='shala',
            order_with_respect_to='ranking',
        ),
    ]