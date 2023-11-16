from django.db import models

class provision(models.Model):
    material_name = models.CharField(max_length=255)
    total_quantity = models.IntegerField()
    utilized_quantity = models.IntegerField()
    balance_quantity = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return self.material_name



class Reintegration(models.Model):
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
        return self.admissionno





class VisitorRegister(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    whom_to_see = models.CharField(max_length=255)
    in_time = models.TimeField()
    out_time = models.TimeField()
    signature = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.date




class PerformanceAppraisal(models.Model):
    month = models.DateField()
    beginning_children = models.IntegerField()
    new_admission = models.IntegerField()
    total_strength = models.IntegerField()
    reintegration = models.IntegerField()
    rehabilitation = models.IntegerField()
    referral = models.IntegerField()
    left = models.IntegerField()
    death = models.IntegerField()
    end_strength = models.IntegerField()
    rescue = models.IntegerField()

    def __str__(self):
        return self.month




class Resident(models.Model):
    pupilName = models.CharField(max_length=255)
    dob = models.DateField()
    morningAttendance = models.CharField(max_length=10, choices=[("present", "Present"), ("absent", "Absent")], null=True, blank=True)
    eveningAttendance = models.CharField(max_length=10, choices=[("present", "Present"), ("absent", "Absent")], null=True, blank=True)
    daysPresent = models.IntegerField()
    schoolFee = models.CharField(max_length=255)
    dayOfPayment = models.CharField(max_length=255)

    def __str__(self):
        return self.pupilName


class SocialEntertainment(models.Model):
    date = models.DateField()
    admission = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    workDetails = models.TextField()

    def __str__(self):
        return self.date




class CaseHistory(models.Model):
    photo = models.ImageField(upload_to='case_history_photos/', null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    religion = models.CharField(max_length=100, blank=True, null=True)
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    maritalStatus = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    identificationMark = models.CharField(max_length=255, blank=True, null=True)
    educationBackground = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    residentContactNumber = models.CharField(max_length=15)
    relativeOrFriendsContact = models.CharField(max_length=15)
    ID_PROOF_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    idProofAvailable = models.CharField(max_length=5, choices=ID_PROOF_CHOICES)
    idProofDetails = models.CharField(max_length=255, blank=True, null=True)
    POLICE_MEMO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    policeMemoAvailable = models.CharField(max_length=5, choices=POLICE_MEMO_CHOICES)
    policeStationDetails = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.photo


class ActionplanRegister(models.Model):
    date_of_plan = models.DateField()
    detailed_notes = models.TextField()
    action_plan_date = models.DateField()

    def __str__(self):
        return self.date_of_plan


class AwarnessRegister(models.Model):
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details = models.TextField()
    participants = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.place} - {self.date}"

class BpPulsenote(models.Model):
    date = models.DateField()
    sno = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pulse = models.IntegerField()
    bp = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.date}"


class CounsellingRegister(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    number_of_sessions = models.IntegerField()
    observation_identification = models.TextField()
    signature = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.date}"


class MedicalCamp(models.Model):
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
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    type_of_disease = models.CharField(max_length=100)
    tablet_details = models.TextField()
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    night = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s Medicine"


class NightSurvey(models.Model):
    date = models.CharField(max_length=255)
    time = models.TimeField()
    place = models.CharField(max_length=255)
    details_of_visit = models.TextField()
    number_of_rescue = models.CharField(max_length=255)

    def __str__(self):
        return f"Night Survey - {self.date}"


class SkillTraining(models.Model):
    sl_no = models.CharField(max_length=255)
    date = models.DateField()
    resident_name = models.CharField(max_length=255)
    skill_training_details = models.TextField()

    def __str__(self):
        return f"Skill Training - {self.sl_no}"


class SmcRegister(models.Model):
    date = models.DateField()
    time = models.TimeField()
    introduction_of_meeting = models.TextField()
    last_month_performance_details = models.TextField()
    issue_resolved = models.BooleanField()
    this_month_issue = models.TextField()
    ngo_staff_name = models.CharField(max_length=255)
    gcc_officials_name = models.CharField(max_length=255)
    police_officials_name = models.CharField(max_length=255)
    residents_name = models.CharField(max_length=255)

    def __str__(self):
        return f"SMC Register - {self.date}"



class StaffAttendence(models.Model):
    sno = models.CharField(max_length=255, verbose_name="SI.No")
    name = models.CharField(max_length=255, verbose_name="Name")
    designation = models.CharField(max_length=255, verbose_name="Designation")
    working_hours = models.TimeField(verbose_name="Working Hours")
    days = models.IntegerField(verbose_name="Days")
    working_days = models.IntegerField(verbose_name="No.of Working Days")
    leave_days = models.IntegerField(verbose_name="No.of Days Leaves")
    remarks = models.TextField(verbose_name="Remarks")

    def __str__(self):
        return f"{self.sno} - {self.name}"


class Stock(models.Model):
    date = models.DateField()
    particulars = models.CharField(max_length=255)
    receipt = models.CharField(max_length=255)
    issued = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.particulars}"


class EmploymentLink(models.Model):
    si_no = models.CharField(max_length=20)
    admission_no = models.CharField(max_length=20)
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



class AccidentRegister(models.Model):
    date = models.DateField()
    inmate_name = models.CharField(max_length=100)
    age_gender = models.CharField(max_length=20)
    accident_condition = models.CharField(max_length=200)
    accident_place = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)

    def __str__(self):
        return self.inmate_name