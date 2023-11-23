from django.db import models


class AlphaNumericField(models.CharField):
    def _init_(self, *args, **kwargs):
        kwargs['max_length'] = 6  # Set fixed max_length for alphanumeric field
        super()._init_(*args, **kwargs)

    @staticmethod
    def generate_alphanumeric():
        alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return alphanumeric.upper()




class provision(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    material_name = models.CharField(max_length=255)
    total_quantity = models.CharField(max_length=255)
    utilized_quantity = models.CharField(max_length=255)
    balance_quantity = models.CharField(max_length=255)
    remarks = models.TextField()

    def __str__(self):
        return str(self.material_name)



class Reintegration(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    admission_no = models.CharField(max_length=255)
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
    name = models.CharField(max_length=255)
    whom_to_see = models.CharField(max_length=255)
    in_time = models.TimeField()
    out_time = models.TimeField()
    signature = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.date)




class PerformanceAppraisal(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date =models.DateField()
    beginning_children = models.IntegerField()
    new_admission = models.IntegerField()
    total_strength = models.IntegerField()
    reintegration = models.CharField(max_length=255)
    rehabilitation = models.CharField(max_length=255)
    referral = models.CharField(max_length=255)
    left = models.CharField(max_length=255)
    death = models.CharField(max_length=255)
    end_strength = models.IntegerField()
    rescue = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date)




class Resident(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    pupilName = models.CharField(max_length=255)
    dob = models.DateField()
    attendance = models.CharField(max_length=255, default='-')
    daysPresent = models.IntegerField()
    schoolFee = models.IntegerField()
    dayOfPayment = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pupilName)


class SocialEntertainment(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    admission = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    workDetails = models.TextField()

    def __str__(self):
        return self.date


class CaseHistory(models.Model):
    photo_url = models.ImageField(upload_to='photos/', blank=True, null=True)
    name = models.CharField(max_length=255)
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
    detailed_notes = models.TextField()
    action_plan_date = models.DateField()

    def __str__(self):
        return str(self.date_of_plan)


class AccidentRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    inmate_name = models.CharField(max_length=100)
    age_gender = models.CharField(max_length=20)
    accident_condition = models.CharField(max_length=200)
    accident_place = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)

    def __str__(self):
        return str(self.inmate_name)


class AwarnesRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details = models.TextField()
    participants = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.place} - {self.date}"


class Asset(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    s_no = models.CharField(max_length=50)
    date_purchase = models.DateField()
    name_asset = models.CharField(max_length=100)
    no_of_items = models.IntegerField()
    cost = models.IntegerField()
    bill_no = models.CharField(max_length=50)
    place_asset = models.CharField(max_length=100)
    owner_asset = models.CharField(max_length=100)
    dispose_date = models.DateField()

    def __str__(self):
        return str(self.name_asset)

class BpPulsenote(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    sno = models.IntegerField()
    name = models.CharField(max_length=255)
    pulse = models.IntegerField()
    bp = models.IntegerField()
    temperature = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date}"


class CounsellingRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    name = models.CharField(max_length=100)
    number_of_sessions = models.IntegerField()
    observation_identification = models.TextField()
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.date}"


class MedicalCamp(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
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
    date = models.CharField(max_length=255)
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details_of_visit = models.TextField()
    number_of_rescue = models.CharField(max_length=255)

    def __str__(self):
        return f"Night Survey - {self.date}"


class SkillTraining(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    sl_no = models.CharField(max_length=255)
    date = models.DateField()
    resident_name = models.CharField(max_length=255)
    skill_training_details = models.TextField()

    def __str__(self):
        return f"Skill Training - {self.sl_no}"


class SmcRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    time = models.TimeField()
    introduction_of_meeting = models.TextField()
    last_month_performance_details = models.TextField()
    issue_resolved = models.TextField()
    this_month_issue = models.TextField()
    ngo_staff_name = models.CharField(max_length=255)
    gcc_officials_name = models.CharField(max_length=255)
    police_officials_name = models.CharField(max_length=255)
    residents_name = models.CharField(max_length=255)

    def __str__(self):
        return f"SMC Register - {self.date}"



class StaffAttendance(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    sno = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    working_hours = models.TimeField()
    days = models.IntegerField()
    working_days = models.IntegerField()
    leave_days = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f"{self.sno} - {self.name}"


class Stock(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date = models.DateField()
    particulars = models.CharField(max_length=255)
    receipt = models.CharField(max_length=255)
    issued = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.particulars}"


class EmploymentLink(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    si_no = models.IntegerField()
    admission_no = models.IntegerField()
    admission_date = models.DateField()
    resident_name = models.CharField(max_length=100)
    employment_name = models.CharField(max_length=100)
    address_and_contact_details = models.TextField()
    designation = models.CharField(max_length=50)
    joining_date = models.DateField()
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.si_no} - {self.resident_name}"


class Rehabitation(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    sno = models.CharField(max_length=50)
    admission_number = models.CharField(max_length=50)
    name_of_the_resident = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField()
    mode_of_rescue = models.CharField(max_length=100)
    mode_of_rehabilitation = models.CharField(max_length=100)
    follow_up = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_the_resident



class DeathRegister(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    sno = models.CharField(max_length=50)
    name_of_the_death_person = models.CharField(max_length=100)
    age_sex = models.CharField(max_length=20)
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
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    sign = models.TextField()

    def __str__(self):
        return str(self.date)


class StaffMovement(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    date_of_plan = models.DateField()
    working_area = models.CharField(max_length=255)
    nature_of_work = models.CharField(max_length=255)
    work_done_by = models.CharField(max_length=255)
    sign = models.TextField()

    def _str_(self):
        return str(self.date_of_plan)



class UserProfile(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)




class MasterRecords(models.Model):
    # uqid = AlphaNumericField(unique=True, editable=False)
    photo_url = models.ImageField(upload_to='photos/', blank=True, null=True)
    S_no = models.IntegerField()
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
        return f"{self.S_no} - {self.name}"




