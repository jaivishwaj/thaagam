# Generated by Django 4.2.7 on 2024-02-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0035_casework'),
    ]

    operations = [
        migrations.AddField(
            model_name='casework',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
