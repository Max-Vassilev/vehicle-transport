# Generated by Django 5.1.3 on 2024-12-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_alter_vehicletransportrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletransportrequest',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]
