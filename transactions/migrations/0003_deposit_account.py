# Generated by Django 3.0.5 on 2020-04-15 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('transactions', '0002_auto_20200410_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
            preserve_default=False,
        ),
    ]