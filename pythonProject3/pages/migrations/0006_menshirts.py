# Generated by Django 3.2.9 on 2021-12-31 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20211230_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='menshirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('describtion', models.TextField()),
                ('publishdate', models.DateField(default=datetime.datetime.now)),
                ('photo', models.ImageField(upload_to='photos')),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-publishdate'],
            },
        ),
    ]
