# Generated by Django 4.2.7 on 2024-02-15 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0014_remove_nightsurvey_uqid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='uqid',
        ),
    ]
