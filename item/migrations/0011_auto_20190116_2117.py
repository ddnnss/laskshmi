# Generated by Django 2.1.5 on 2019-01-16 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_auto_20190115_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 21, 17, 51, 272609), verbose_name='Срок действия безлимитного кода'),
        ),
    ]
