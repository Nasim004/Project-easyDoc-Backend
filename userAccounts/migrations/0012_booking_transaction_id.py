# Generated by Django 4.1.7 on 2023-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0011_remove_user_district_remove_user_muncipality'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='transaction_id',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
