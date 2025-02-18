# Generated by Django 5.1 on 2024-09-03 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_reservationdetails_guest_reservationdetails_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Cash payment', 'Cash payment'), ('Card Payment', 'Card Payment'), ('Bank Transfer', 'Bamk Transfer')], max_length=100)),
                ('amount', models.FloatField()),
                ('payment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50)),
                ('reservation_det', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.reservationdetails')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('payments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.payment')),
            ],
        ),
    ]
