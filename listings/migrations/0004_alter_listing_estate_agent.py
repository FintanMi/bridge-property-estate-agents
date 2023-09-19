# Generated by Django 3.2.20 on 2023-09-19 15:57

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0003_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='estate_agent',
            field=models.ForeignKey(default=builtins.id, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]
