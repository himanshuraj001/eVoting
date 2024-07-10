# Generated by Django 3.1.7 on 2021-03-21 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoting_app', '0008_auto_20210321_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('mobile', models.IntegerField()),
                ('aadhar_number', models.CharField(max_length=12)),
                ('register_date', models.DateField(default=datetime.datetime(2021, 3, 21, 16, 28, 5, 598507))),
                ('dob', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 16, 28, 5, 597462)),
        ),
    ]
