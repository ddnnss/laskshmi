# Generated by Django 2.1.5 on 2019-01-15 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20190115_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен?'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 20, 52, 42, 10688), verbose_name='Срок действия безлимитного кода'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='promo_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Промокод (для создания рандомного значения оставить пустым)'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='promo_discount',
            field=models.IntegerField(default=0, verbose_name='Скидка на заказ'),
        ),
    ]
