# Generated by Django 4.2.7 on 2024-02-19 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0023_masterrecords_action_takenup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterrecords',
            name='Second_Follow_Up',
        ),
    ]
