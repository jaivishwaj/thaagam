from django import forms
from .models import provision,Reintegration,VisitorRegister,PerformanceAppraisal,Resident,SocialEntertainment,CaseHistory,ActionplanRegister,AwarnesRegister,BpPulsenote,CounsellingRegister,MedicalCamp,Medicine,NightSurvey,SkillTraining,SmcRegister,StaffAttendance,Stock,EmploymentLink,Rehabitation,DeathRegister,AccidentRegister

class ProvisionForm(forms.ModelForm):
    class Meta:
        model = provision
        fields = '__all__'

class ReintegrationForm(forms.ModelForm):
    class Meta:
        models = Reintegration
        fields = '__all__'


class VisitorRegisterForm(forms.ModelForm):
    class Meta:
        models = VisitorRegister
        fields = '__all__'


class PerformanceAppraisalForm(forms.ModelForm):
    class Meta:
        models = PerformanceAppraisal
        fields = '__all__'


class ResidentForm(forms.ModelForm):
    class Meta:
        models = Resident
        fields = '__all__'


class SocialEntertainmentForm(forms.ModelForm):
    class Meta:
        models = SocialEntertainment
        fields = '__all__'


class CaseHistoryForm(forms.ModelForm):
    class Meta:
        models = CaseHistory
        fields = '__all__'


class ActionplanRegisterForm(forms.ModelForm):
    class Meta:
        models = ActionplanRegister
        fields = '__all__'


class AwarnesRegisterForm(forms.ModelForm):
    class Meta:
        models = AwarnesRegister
        fields = '__all__'


class BpPulsenote(forms.ModelForm):
    class Meta:
        models = BpPulsenote
        fields = '__all__'



class CounsellingForm(forms.ModelForm):
    class Meta:
        models = CounsellingRegister
        fields = '__all__'


class MedicalCampForm(forms.ModelForm):
    class Meta:
        models = MedicalCamp
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        models = Medicine
        fields = '__all__'


class NightSurveyForms(forms.ModelForm):
    class Meta:
        models = NightSurvey
        fields = '__all__'

class SkillTrainingForms(forms.ModelForm):
    class Meta:
        models = SkillTraining
        fields = '__all__'


class SmcRegisterForms(forms.ModelForm):
    class Meta:
        models = SmcRegister
        fields = '__all__'


class StaffAttendanceForms(forms.ModelForm):
    class Meta:
        models = StaffAttendance
        fields = '__all__'


class StockForms(forms.ModelForm):
    class Meta:
        models = Stock
        fields = '__all__'


class EmploymentLinkForms(forms.ModelForm):
    class Meta:
        models = Stock
        fields = '__all__'

class RehabitationForms(forms.ModelForm):
    class Meta:
        model = Rehabitation
        fields = '__all__'


class DeathRegisterForms(forms.ModelForm):
    class Meta:
        model = DeathRegister
        fields = '__all__'


class AccidentRegisterForms(forms.ModelForm):
    class Meta:
        model = AccidentRegister
        fields = '__all__'


