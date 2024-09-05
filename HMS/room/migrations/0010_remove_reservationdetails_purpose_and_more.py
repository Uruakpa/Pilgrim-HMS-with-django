# Generated by Django 5.1 on 2024-09-05 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_alter_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationdetails',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='reservationdetails',
            name='remarks',
        ),
        migrations.AddField(
            model_name='guestdetails',
            name='contact_det',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.contactdetails'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/roomimages'),
        ),
        migrations.AlterField(
            model_name='reservationdetails',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.roomdetails'),
        ),
    ]
