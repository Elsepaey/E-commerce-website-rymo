# Generated by Django 3.2.9 on 2021-12-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_bags_dresses_watches'),
    ]

    operations = [
        migrations.AddField(
            model_name='bags',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dresses',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shoes',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='watches',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
