# Generated by Django 3.2.5 on 2021-09-18 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210916_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 18, 10, 24, 14, 541832)),
        ),
    ]
