# Generated by Django 4.1.7 on 2023-04-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0009_alter_booking_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='token',
            field=models.CharField(max_length=20),
        ),
    ]
