# Generated by Django 4.0 on 2021-12-15 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pvision.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('birthdate', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('gender', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Male'), (2, 'Female')], default=0)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('zipcode', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eye', models.IntegerField(choices=[(1, 'left'), (2, 'right'), (0, 'Unknown')], default=0)),
                ('date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('result', models.JSONField(default=pvision.models.Measurement.result_default)),
                ('program', models.CharField(default='NaN', max_length=2560)),
                ('comment', models.CharField(blank=True, default='', max_length=2560)),
                ('measurement_done', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvision.patient')),
            ],
        ),
    ]
