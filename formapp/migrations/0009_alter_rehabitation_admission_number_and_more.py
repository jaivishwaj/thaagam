# Generated by Django 4.1.12 on 2023-11-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_alter_nightsurvey_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehabitation',
            name='admission_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rehabitation',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rehabitation',
            name='sno',
            field=models.IntegerField(),
        ),
    ]
