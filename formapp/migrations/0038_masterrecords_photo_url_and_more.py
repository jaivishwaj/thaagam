# Generated by Django 4.2.7 on 2023-11-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0037_alter_casehistory_address_alter_casehistory_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterrecords',
            name='photo_url',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='idProofAvailable',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='policeMemoAvailable',
            field=models.CharField(max_length=255),
        ),
    ]