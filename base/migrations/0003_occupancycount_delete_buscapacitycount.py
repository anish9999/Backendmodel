# Generated by Django 4.1.7 on 2023-02-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_buscapacitycount'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupancyCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus_id', models.IntegerField()),
                ('Total_count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BusCapacityCount',
        ),
    ]