# Generated by Django 4.2.7 on 2023-11-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0010_alter_asset_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bppulsenote',
            name='bp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bppulsenote',
            name='sno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bppulsenote',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]