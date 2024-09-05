# Generated by Django 5.0.3 on 2024-09-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_reservationdetails_room_det_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Booked', 'Booked')], max_length=50, null=True),
        ),
    ]
