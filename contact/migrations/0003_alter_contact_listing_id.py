# Generated by Django 3.2.20 on 2023-09-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(null=True),
        ),
    ]
