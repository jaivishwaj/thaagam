# Generated by Django 4.2.7 on 2024-02-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0036_casework_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='casework',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
