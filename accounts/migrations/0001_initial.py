# Generated by Django 3.0.5 on 2020-04-10 01:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField(default=10000000, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('balance', models.FloatField(default=0)),
                ('account_type', models.CharField(choices=[('SAVINGS', 'Savings'), ('CURRENT', 'Current')], default='SAVINGS', max_length=100)),
                ('currency', models.CharField(choices=[('KENYA SHILLINGS', 'Kenya Shillings'), ('US DOLLAR', 'US Dollars')], default='KENYA SHILLINGS', max_length=15)),
            ],
            options={
                'db_table': 'tbl_Accounts',
            },
        ),
    ]