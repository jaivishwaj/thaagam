# Generated by Django 4.1.12 on 2023-12-03 07:11

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formapp', '0002_delete_accidentregister_delete_actionplanregister_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqid', models.IntegerField()),
                ('date', models.DateField()),
                ('inmate_name', models.CharField(max_length=100)),
                ('age_gender', models.IntegerField()),
                ('accident_condition', models.CharField(max_length=200)),
                ('accident_place', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ActionplanRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_plan', models.DateField()),
                ('detailed_notes', models.TextField()),
                ('action_plan_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchase', models.DateField()),
                ('uqid', models.IntegerField()),
                ('name_asset', models.CharField(max_length=100)),
                ('no_of_items', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('bill_no', models.IntegerField()),
                ('place_asset', models.CharField(max_length=100)),
                ('owner_asset', models.CharField(max_length=100)),
                ('dispose_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AwarnesRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('place', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('participants', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BpPulsenote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('pulse', models.IntegerField()),
                ('bp', models.IntegerField()),
                ('temperature', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('religion', models.CharField(max_length=255)),
                ('maritalStatus', models.CharField(max_length=50)),
                ('identificationMark', models.TextField()),
                ('educationBackground', models.TextField()),
                ('occupation', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('residentContactNumber', models.CharField(max_length=15)),
                ('relativeOrFriendsContact', models.CharField(max_length=15)),
                ('idProofAvailable', models.CharField(max_length=255)),
                ('idProofDetails', models.TextField()),
                ('policeMemoAvailable', models.CharField(max_length=255)),
                ('policeStationDetails', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CounsellingRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('number_of_sessions', models.IntegerField()),
                ('observation_identification', models.TextField()),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeathRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqid', models.IntegerField()),
                ('name_of_the_death_person', models.CharField(max_length=100)),
                ('age_sex', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_death', models.DateField()),
                ('reason_for_death', models.CharField(max_length=200)),
                ('whom_to_claim_death_person', models.CharField(max_length=100)),
                ('address_and_contact_number', models.CharField(max_length=200)),
                ('legal_producer_taken_if_unclaimed', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqid', models.IntegerField()),
                ('admission_no', models.IntegerField()),
                ('admission_date', models.DateField()),
                ('resident_name', models.CharField(max_length=100)),
                ('employment_name', models.CharField(max_length=100)),
                ('address_and_contact_details', models.TextField()),
                ('designation', models.CharField(max_length=50)),
                ('joining_date', models.DateField()),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('morning_snacks', models.CharField(max_length=100)),
                ('no_of_resident1', models.IntegerField()),
                ('breakfast', models.CharField(max_length=100)),
                ('no_of_resident2', models.IntegerField()),
                ('lunch', models.CharField(max_length=100)),
                ('no_of_resident3', models.IntegerField()),
                ('dinner', models.CharField(max_length=100)),
                ('no_of_resident4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inspectionregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('sign', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MasterRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('Aid_no', models.IntegerField()),
                ('Age_gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('Date_Of_Admission', models.DateField()),
                ('Date_Of_Leaving', models.DateField()),
                ('Family_Contact_No', models.CharField(max_length=20)),
                ('Relation', models.CharField(max_length=50)),
                ('Permanent_Address', models.TextField()),
                ('Mode_Of_Identification_Rescue', models.CharField(max_length=100)),
                ('Identification_Mark', models.CharField(max_length=100)),
                ('Identification_Papers', models.CharField(max_length=100)),
                ('Rehabilitation_Measures', models.TextField()),
                ('Reason_For_Leaving_Shelter', models.TextField()),
                ('Follow_Up_Action', models.TextField()),
                ('Second_Follow_Up', models.TextField()),
                ('Medical_Status', models.CharField(max_length=50)),
                ('File_Closure_Status', models.CharField(max_length=50)),
                ('Remarks', models.TextField()),
                ('Signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('complaints', models.TextField()),
                ('others', models.TextField(blank=True)),
                ('treatment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uqid', models.IntegerField()),
                ('age', models.IntegerField()),
                ('type_of_disease', models.CharField(max_length=100)),
                ('tablet_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NightSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('time', models.TimeField()),
                ('place', models.CharField(max_length=255)),
                ('details_of_visit', models.TextField()),
                ('number_of_rescue', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceAppraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('beginning_children', models.IntegerField()),
                ('new_admission', models.CharField(max_length=100)),
                ('total_strength', models.IntegerField()),
                ('reintegration', models.CharField(max_length=100)),
                ('rehabilitation', models.CharField(max_length=100)),
                ('referral', models.CharField(max_length=100)),
                ('left', models.CharField(max_length=100)),
                ('death', models.CharField(max_length=100)),
                ('end_strength', models.IntegerField()),
                ('rescue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('uqid', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('street_address', models.CharField(default='', max_length=150)),
                ('street_address_2', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state_province', models.CharField(default='', max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('home_phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='provision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255)),
                ('total_quantity', models.IntegerField()),
                ('utilized_quantity', models.IntegerField()),
                ('balance_quantity', models.IntegerField()),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rehabitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqid', models.IntegerField()),
                ('admission_number', models.CharField(max_length=50)),
                ('name_of_the_resident', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('date_of_joining', models.DateField()),
                ('date_of_leaving', models.DateField()),
                ('mode_of_rescue', models.CharField(max_length=100)),
                ('mode_of_rehabilitation', models.CharField(max_length=100)),
                ('follow_up', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reintegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.IntegerField()),
                ('uqid', models.IntegerField()),
                ('resident_name', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('reason_for_leaving', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('follow_up_conduct', models.TextField()),
                ('follows', models.CharField(max_length=255)),
                ('staff_event_close', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupilName', models.CharField(max_length=100)),
                ('uqid', models.IntegerField()),
                ('dob', models.DateField()),
                ('attendance', models.CharField(default='-', max_length=255)),
                ('daysPresent', models.IntegerField()),
                ('schoolFee', models.IntegerField()),
                ('dayOfPayment', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaryRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('sign', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('resident_name', models.CharField(max_length=100)),
                ('skill_training_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SmcRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('introduction_of_meeting', models.TextField()),
                ('last_month_performance_details', models.TextField()),
                ('issue_resolved', models.TextField()),
                ('this_month_issue', models.TextField()),
                ('ngo_staff_name', models.CharField(max_length=100)),
                ('gcc_officials_name', models.CharField(max_length=100)),
                ('police_officials_name', models.CharField(max_length=100)),
                ('residents_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SocialEntertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('admission', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('workDetails', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uqid', models.IntegerField()),
                ('designation', models.CharField(max_length=255)),
                ('working_hours', models.TimeField()),
                ('days', models.IntegerField()),
                ('working_days', models.IntegerField()),
                ('leave_days', models.IntegerField()),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_plan', models.DateField()),
                ('uqid', models.IntegerField()),
                ('working_area', models.CharField(max_length=255)),
                ('nature_of_work', models.CharField(max_length=255)),
                ('work_done_by', models.CharField(max_length=255)),
                ('sign', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('particulars', models.CharField(max_length=255)),
                ('receipt', models.CharField(max_length=255)),
                ('issued', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('confrimpassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('uqid', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('whom_to_see', models.CharField(max_length=255)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')])),
                ('signature', models.TextField()),
            ],
        ),
    ]
