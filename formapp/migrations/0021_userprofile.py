# Generated by Django 4.2.7 on 2023-11-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0020_remove_medicine_afternoon_remove_medicine_morning_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]