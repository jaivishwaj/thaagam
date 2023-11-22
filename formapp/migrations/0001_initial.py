# Generated by Django 4.2.7 on 2023-11-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255)),
                ('total_quantity', models.IntegerField()),
                ('utilized_quantity', models.IntegerField()),
                ('balance_quantity', models.IntegerField()),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reintegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=255)),
                ('resident_name', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('reason_for_leaving', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('follow_up_conduct', models.TextField()),
                ('follows', models.CharField(max_length=255)),
                ('staff_event_close', models.CharField(max_length=255)),
            ],
        ),
    ]