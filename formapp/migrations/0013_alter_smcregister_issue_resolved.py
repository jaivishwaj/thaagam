# Generated by Django 4.1.12 on 2023-11-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0012_alter_deathregister_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smcregister',
            name='issue_resolved',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3),
        ),
    ]
