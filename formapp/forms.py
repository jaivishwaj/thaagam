from django import forms

from django.forms import ModelForm
from .models import *
 
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


class AwarnessRegisterForm(forms.ModelForm):
    class Meta:
        models = AwarnesRegister
        fields = '__all__'


class BpPulsenoteForm(forms.ModelForm):
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


class NightSurveyForm(forms.ModelForm):
    class Meta:
        models = NightSurvey
        fields = '__all__'

class SkillTrainingForm(forms.ModelForm):
    class Meta:
        models = SkillTraining
        fields = '__all__'


class SmcRegisterForm(forms.ModelForm):
    class Meta:
        models = SmcRegister
        fields = '__all__'


class StaffAttendenceForm(forms.ModelForm):
    class Meta:
        models = StaffAttendance
        fields = '__all__'


class StockForm(forms.ModelForm):
    class Meta:
        models = Stock
        fields = '__all__'


class EmploymentLinkForm(forms.ModelForm):
    class Meta:
        models = EmploymentLink
        fields = '__all__'

class RehabitationForm(forms.ModelForm):
    class Meta:
        model = Rehabitation
        fields = '__all__'


class DeathRegisterForm(forms.ModelForm):
    class Meta:
        model = DeathRegister
        fields = '__all__'


class AccidentRegisterForm(forms.ModelForm):
    class Meta:
        model = AccidentRegister
        fields = '__all__'





class CaseWorkForm(forms.ModelForm):
    class Meta:
        model = CaseWork
        fields = '__all__'
        
        
class FollowUPForm(forms.ModelForm):
    class Meta:
        model = FollowUP
        fields = '__all__'