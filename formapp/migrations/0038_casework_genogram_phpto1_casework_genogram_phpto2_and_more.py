# Generated by Django 4.2.7 on 2024-02-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0037_casework_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='casework',
            name='genogram_phpto1',
            field=models.ImageField(blank=True, null=True, upload_to='genograms1/'),
        ),
        migrations.AddField(
            model_name='casework',
            name='genogram_phpto2',
            field=models.ImageField(blank=True, null=True, upload_to='genograms2/'),
        ),
        migrations.AddField(
            model_name='casework',
            name='reason_for_homeless_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='homeless_photos1/'),
        ),
        migrations.AddField(
            model_name='casework',
            name='reason_for_homeless_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='homeless_photos2/'),
        ),
        migrations.AlterField(
            model_name='casework',
            name='genogram',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='casework',
            name='res_letter',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='casework',
            name='res_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='res_photos1/'),
        ),
        migrations.AlterField(
            model_name='casework',
            name='res_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='res_photos2/'),
        ),
    ]
