# Generated by Django 4.2.7 on 2024-02-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidentregister',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='asset',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='bppulsenote',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='counsellingregister',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='employmentlink',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='masterrecords',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='medicalcamp',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='nightsurvey',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='performanceappraisal',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='rehabitation',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='reintegration',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='resident',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='salaryregister',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='socialentertainment',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='staffattendance',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='visitorregister',
            name='uqid',
            field=models.CharField(max_length=4),
        ),
    ]
