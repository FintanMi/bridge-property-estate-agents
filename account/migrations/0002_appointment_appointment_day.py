# Generated by Django 3.2.20 on 2023-09-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_day',
            field=models.DateTimeField(default=False),
        ),
    ]
