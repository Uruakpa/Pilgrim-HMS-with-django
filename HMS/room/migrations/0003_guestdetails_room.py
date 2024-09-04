# Generated by Django 5.1 on 2024-09-03 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_guestdetails_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestdetails',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.rooms'),
        ),
    ]
