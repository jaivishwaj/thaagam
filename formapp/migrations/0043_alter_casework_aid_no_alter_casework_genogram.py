# Generated by Django 4.2.7 on 2024-02-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0042_casework_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casework',
            name='aid_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='casework',
            name='genogram',
            field=models.CharField(max_length=100, null=True),
        ),
    ]