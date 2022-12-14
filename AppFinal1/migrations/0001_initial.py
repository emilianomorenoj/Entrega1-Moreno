# Generated by Django 4.1.1 on 2022-09-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikeinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biketype', models.CharField(max_length=60)),
                ('wheelsize', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='RacingVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('racetype', models.CharField(max_length=60)),
                ('racelevel', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='RiderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('dateofbirth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
