# Generated by Django 4.2.7 on 2024-02-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0031_alter_rehabitation_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehabitation',
            name='photo_url',
            field=models.ImageField(blank=True, null=True, upload_to='rehabitation_photos/'),
        ),
    ]