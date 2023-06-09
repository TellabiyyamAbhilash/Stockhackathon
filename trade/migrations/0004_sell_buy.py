# Generated by Django 4.1.9 on 2023-05-14 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mis', models.BooleanField(default=True)),
                ('on_nrml', models.BooleanField(default=False)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('lots', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('market', models.BooleanField(default=True)),
                ('limit', models.BooleanField(default=False)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.stocks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mis', models.BooleanField(default=True)),
                ('on_nrml', models.BooleanField(default=False)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('lots', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('market', models.BooleanField(default=True)),
                ('limit', models.BooleanField(default=False)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.stocks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
