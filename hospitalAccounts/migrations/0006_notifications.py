# Generated by Django 4.1.7 on 2023-03-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAccounts', '0005_doctor_tokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
