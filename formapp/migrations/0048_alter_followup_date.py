# Generated by Django 4.2.7 on 2024-02-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0047_followup_date_alter_followup_uqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
