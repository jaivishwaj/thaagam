from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# class AlphaNumericField(models.CharField):
#     def _init_(self, *args, **kwargs):
#         kwargs['max_length'] = 6  # Set fixed max_length for alphanumeric field
#         super()._init_(*args, **kwargs)
#
#     @staticmethod
#     def generate_alphanumeric():
#         alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#         return alphanumeric.upper()

class Inspectionregister(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    sign = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class provision(models.Model):
    material_name = models.CharField(max_length=255)
    user = models.CharField(max_length=200)
    total_quantity = models.IntegerField()
    utilized_quantity = models.IntegerField()
    balance_quantity = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return str(self.material_name)













class Reintegration(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    admission_no = models.IntegerField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    resident_name = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField(null=True, blank=True)
    reason_for_leaving = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    follow_up_conduct = models.TextField()
    follows = models.CharField(max_length=255)
    staff_event_close = models.CharField(max_length=255)

    def __str__(self):
        return str(self.admission_no)





class VisitorRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=255)
    whom_to_see = models.CharField(max_length=255)
    in_time = models.TimeField()
    out_time = models.TimeField()

    phone_regex = RegexValidator(
        regex=r'^\d{10}$',  # Validates 10 digits
        message="Phone number must be 10 digits.",
    )
    phone_number = models.CharField(max_length=10, validators=[phone_regex])
    signature = models.TextField()

    def __str__(self):
        return str(self.date)




class PerformanceAppraisal(models.Model):
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    beginning_children = models.IntegerField()
    new_admission = models.CharField(max_length=100)
    total_strength = models.IntegerField()
    reintegration = models.CharField(max_length=100)
    rehabilitation = models.CharField(max_length=100)
    referral = models.CharField(max_length=100)
    left = models.CharField(max_length=100)
    death = models.CharField(max_length=100)
    end_strength = models.IntegerField()
    rescue = models.IntegerField()

    def __str__(self):
        return str(self.date)




class Resident(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    pupilName = models.CharField(max_length=100)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    dob = models.DateField()
    attendance = models.CharField(max_length=255, default='-')
    daysPresent = models.IntegerField()
    schoolFee = models.IntegerField()
    dayOfPayment = models.DateField()

    def __str__(self):
        return str(self.pupilName)


class SocialEntertainment(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    admission = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    workDetails = models.TextField()

    def __str__(self):
        return self.date


class CaseHistory(models.Model):
    photo_url = models.ImageField(upload_to='photos/', blank=True, null=True)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    religion = models.CharField(max_length=255)
    maritalStatus = models.CharField(max_length=50)
    identificationMark = models.TextField()
    educationBackground = models.TextField()
    occupation = models.CharField(max_length=255)
    address = models.TextField()
    residentContactNumber = models.CharField(max_length=15)
    relativeOrFriendsContact = models.CharField(max_length=15)
    idProofAvailable = models.CharField(max_length=255)
    idProofDetails = models.TextField()
    policeMemoAvailable = models.CharField(max_length=255)
    policeStationDetails = models.TextField()

    def __str__(self):
        return self.name




#
# class CaseHistory(models.Model):
#     # uqid = AlphaNumericField(unique=True, editable=False)
#     photo_url = models.URLField(null=True, blank=True)
#     # photo = models.ImageField(upload_to='case_history_photos/', null=True, blank=True)
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     SEX_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ]
#     sex = models.CharField(max_length=10, choices=SEX_CHOICES)
#     religion = models.CharField(max_length=100, blank=True, null=True)
#     MARITAL_STATUS_CHOICES = [
#         ('single', 'Single'),
#         ('married', 'Married'),
#         ('divorced', 'Divorced'),
#         ('widowed', 'Widowed'),
#     ]
#     maritalStatus = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
#     identificationMark = models.CharField(max_length=255, blank=True, null=True)
#     educationBackground = models.CharField(max_length=255, blank=True, null=True)
#     occupation = models.CharField(max_length=255, blank=True, null=True)
#     address = models.TextField()
#     residentContactNumber = models.CharField(max_length=15)
#     relativeOrFriendsContact = models.CharField(max_length=15)
#     ID_PROOF_CHOICES = [
#         ('yes', 'Yes'),
#         ('no', 'No'),
#     ]
#     idProofAvailable = models.CharField(max_length=5, choices=ID_PROOF_CHOICES)
#     idProofDetails = models.CharField(max_length=255, blank=True, null=True)
#     POLICE_MEMO_CHOICES = [
#         ('yes', 'Yes'),
#         ('no', 'No'),
#     ]
#     policeMemoAvailable = models.CharField(max_length=5, choices=POLICE_MEMO_CHOICES)
#     policeStationDetails = models.CharField(max_length=255, blank=True, null=True)
#
#
#     def __str__(self):
#         return str(self.photo)


class ActionplanRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)

    date_of_plan = models.DateField()
    user = models.CharField(max_length=200)
    detailed_notes = models.TextField()
    action_plan_date = models.DateField()

    def __str__(self):
        return str(self.date_of_plan)


class AccidentRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    user = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    date = models.DateField()
    inmate_name = models.CharField(max_length=100)
    age_gender = models.IntegerField()
    accident_condition = models.CharField(max_length=200)
    accident_place = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)

    def __str__(self):
        return str(self.uqid)

class AwarnesRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details = models.TextField()
    participants = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.place} - {self.date}"


class Asset(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date_purchase = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name_asset = models.CharField(max_length=100)
    no_of_items = models.IntegerField()
    cost = models.IntegerField()
    bill_no = models.IntegerField()
    place_asset = models.CharField(max_length=100)
    owner_asset = models.CharField(max_length=100)
    dispose_date = models.DateField()

    def __str__(self):
        return str(self.name_asset)

class BpPulsenote(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=100)
    pulse = models.IntegerField()
    bp = models.IntegerField()
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.date}"


class CounsellingRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=100)
    number_of_sessions = models.IntegerField()
    observation_identification = models.TextField()
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.date}"


class MedicalCamp(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    complaints = models.TextField()
    others = models.TextField(blank=True)
    treatment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}'s Medical Camp"


class Medicine(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    age = models.IntegerField()
    type_of_disease = models.CharField(max_length=100)
    tablet_details = models.TextField()
    # morning = models.BooleanField(default=False)
    # afternoon = models.BooleanField(default=False)
    # night = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s Medicine"


class NightSurvey(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details_of_visit = models.TextField()
    number_of_rescue = models.CharField(max_length=255)

    def __str__(self):
        return f"Night Survey - {self.date}"

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, default="")
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    date = models.DateField(default=timezone.now)
    street_address = models.CharField(max_length=150, default="")
    street_address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, default="")
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    home_phone_number = models.CharField(max_length=20, default="", blank=True)
    email = models.EmailField()
    birthdate = models.DateField(default=timezone.now)
    photo_url = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        date_info = self.date.strftime('%Y-%m-%d') if self.date else "No Date"
        return f"{self.name} - {date_info}"

class SkillTraining(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    resident_name = models.CharField(max_length=100)
    skill_training_details = models.TextField()

    def __str__(self):
        return f"Skill Training - {self.date}"






class SmcRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    time = models.TimeField()
    introduction_of_meeting = models.TextField()
    last_month_performance_details = models.TextField()
    issue_resolved = models.TextField()
    this_month_issue = models.TextField()
    ngo_staff_name = models.CharField(max_length=100)
    gcc_officials_name = models.CharField(max_length=100)
    police_officials_name = models.CharField(max_length=100)
    residents_name = models.CharField(max_length=100)

    def __str__(self):
        return f"SMC Register - {self.date}"



class StaffAttendance(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)

    name = models.CharField(max_length=100)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    designation = models.CharField(max_length=255)
    working_hours = models.TimeField()
    days = models.IntegerField()
    working_days = models.IntegerField()
    leave_days = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return str(self.name)


class Stock(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    particulars = models.CharField(max_length=255)
    receipt = models.CharField(max_length=255)
    issued = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.particulars}"


class EmploymentLink(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    uqid = models.IntegerField()
    user = models.CharField(max_length=200)
    admission_no = models.IntegerField()
    admission_date = models.DateField()
    resident_name = models.CharField(max_length=100)
    employment_name = models.CharField(max_length=100)
    address_and_contact_details = models.TextField()
    designation = models.CharField(max_length=50)
    joining_date = models.DateField()
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.uqid} - {self.resident_name}"


class Rehabitation(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    uqid = models.IntegerField()
    user = models.CharField(max_length=200)
    admission_number = models.CharField(max_length=50)
    name_of_the_resident = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField()
    mode_of_rescue = models.CharField(max_length=100)
    mode_of_rehabilitation = models.CharField(max_length=100)
    follow_up = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_the_resident



class DeathRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    uqid = models.IntegerField()
    user = models.CharField(max_length=200)
    name_of_the_death_person = models.CharField(max_length=100)
    age_sex = models.CharField(max_length=20, null=True, blank=True)
    date_of_death = models.DateField()
    reason_for_death = models.CharField(max_length=200)
    whom_to_claim_death_person = models.CharField(max_length=100)
    address_and_contact_number = models.CharField(max_length=200)
    legal_producer_taken_if_unclaimed = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_the_death_person



class FoodMenu(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    morning_snacks = models.CharField(max_length=100)
    no_of_resident1 = models.IntegerField()
    breakfast = models.CharField(max_length=100)
    no_of_resident2 = models.IntegerField()
    lunch = models.CharField(max_length=100)
    no_of_resident3 = models.IntegerField()
    dinner = models.CharField(max_length=100)
    no_of_resident4 = models.IntegerField()

    def __str__(self):
        return str(self.date)



class SalaryRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    sign = models.TextField()

    def __str__(self):
        return str(self.date)


class StaffMovement(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date_of_plan = models.DateField()
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    working_area = models.CharField(max_length=255)
    nature_of_work = models.CharField(max_length=255)
    work_done_by = models.CharField(max_length=255)
    sign = models.TextField()

    def _str_(self):
        return str(self.date_of_plan)


class userprofile(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    username = models.CharField(max_length=50)
    user = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile_number = models.IntegerField()
    password = models.CharField(max_length=50)
    confrimpassword = models.CharField(max_length=50)

    #
    def __str__(self):
        return str(self.username)










class MasterRecords(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    photo_url = models.ImageField(upload_to='photos/', blank=True, null=True)
    user = models.CharField(max_length=200)
    uqid = models.IntegerField()
    name = models.CharField(max_length=100)
    Aid_no = models.IntegerField()
    Age_gender = models.CharField(max_length=50)
    dob = models.DateField()
    Date_Of_Admission = models.DateField()
    Date_Of_Leaving = models.DateField()
    Family_Contact_No = models.CharField(max_length=20)
    Relation = models.CharField(max_length=50)
    Permanent_Address = models.TextField()
    Mode_Of_Identification_Rescue = models.CharField(max_length=100)
    Identification_Mark = models.CharField(max_length=100)
    Identification_Papers = models.CharField(max_length=100)
    Rehabilitation_Measures = models.TextField()
    Reason_For_Leaving_Shelter = models.TextField()
    Follow_Up_Action = models.TextField()
    Second_Follow_Up = models.TextField()
    Medical_Status = models.CharField(max_length=50)
    File_Closure_Status = models.CharField(max_length=50)
    Remarks = models.TextField()
    Signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.uqid} - {self.name}"




