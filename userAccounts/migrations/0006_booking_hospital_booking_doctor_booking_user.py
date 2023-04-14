# Generated by Django 4.1.7 on 2023-04-13 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAccounts', '0009_doctor_fee'),
        ('userAccounts', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Hospital',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hospitalAccounts.hospital'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hospitalAccounts.doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='userAccounts.user'),
            preserve_default=False,
        ),
    ]