# Generated by Django 4.2.7 on 2024-02-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0016_remove_visitorregister_uqid'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentregister',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
