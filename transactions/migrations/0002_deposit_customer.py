# Generated by Django 3.0.5 on 2020-04-10 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
    ]
