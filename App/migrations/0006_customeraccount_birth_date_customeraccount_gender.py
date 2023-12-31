# Generated by Django 4.1.6 on 2023-06-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_customeraccount_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccount',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customeraccount',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
    ]
