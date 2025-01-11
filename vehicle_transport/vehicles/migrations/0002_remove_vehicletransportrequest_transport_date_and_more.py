# Generated by Django 5.1.3 on 2024-11-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicletransportrequest',
            name='transport_date',
        ),
        migrations.RemoveField(
            model_name='vehicletransportrequest',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='vehicletransportrequest',
            name='big_car_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicletransportrequest',
            name='bus_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicletransportrequest',
            name='final_sum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='vehicletransportrequest',
            name='small_car_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicletransportrequest',
            name='suv_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
