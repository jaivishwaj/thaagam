# Generated by Django 4.1.12 on 2023-11-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0009_alter_rehabitation_admission_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentlink',
            name='admission_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employmentlink',
            name='si_no',
            field=models.IntegerField(),
        ),
    ]
