# Generated by Django 4.1.7 on 2023-02-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0002_rename_number_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
