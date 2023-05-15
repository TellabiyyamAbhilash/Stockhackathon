# Generated by Django 4.1.9 on 2023-05-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_sell_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='sell',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]