# Generated by Django 4.2.7 on 2023-11-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0005_alter_performanceappraisal_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performanceappraisal',
            name='month',
            field=models.DateField(),
        ),
    ]