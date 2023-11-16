from django.shortcuts import render,redirect
from .forms import ProvisionForm,ReintegrationForm,VisitorRegister,PerformanceAppraisal,Resident,SocialEntertainment,CaseHistory,ActionplanRegister,AwarnessRegister,BpPulsenote,CounsellingRegister,MedicalCamp,Medicine,NightSurvey,SkillTraining,SmcRegister,StaffAttendence,Stock,EmploymentLink,Rehabitation,DeathRegister,AccidentRegister
from .models import provision
def provision_form(request):
    if request.method == 'POST':
        materialName = request.POST.get('materialName')
        totalQuantity = request.POST.get('totalQuantity')
        utilizedQuantity = request.POST.get('utilizedQuantity')
        balanceQuantity = request.POST.get('balanceQuantity')
        remarks = request.POST.get('remarks')
        datas = provision.objects.create(material_name=materialName,total_quantity=totalQuantity,utilized_quantity=utilizedQuantity,balance_quantity=balanceQuantity,remarks=remarks)
        datas.save()
        return redirect('success')

    return render(request,'provision.html')

def dashboard(request):
    datas = provision.objects.all()
    return render(request, 'dashboard.html',{'data':datas})

def reintegration_form(request):
    if request.method == 'POST':
        form = ReintegrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'reintegration')


    return render(request,'reintegration.html')

def visitor_register_form(request):
    if request.method == 'POST':
        form = VisitorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'visitor_register.html')

    return render(request,'visitor_register.html')


def performance_appraisal_form(request):
    if request.method == 'POST':
        form = PerformanceAppraisalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'performance_appraisal.html')

    return render(request,'performance_appraisal.html')


def resident_form(request):
    if request.method == 'POST':
        form = ResidentForm(request.POSt)
        if form.is_valid():
            form.save()
            return redirect(request,'resident.html')

    return render(request,'resident.html')


def social_entertainment_form(request):
    if request.method == 'POST':
        form = SocialEntertainmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'social_entertainment.html')

    return render(request,'social_entertainment.html')



def case_history_form(request):
    if request.method == 'POST':
        form = CaseHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'case_history.html')


    return render(request,'case_history.html')



def actionplan_register_form(request):
    if request.method == 'POST':
        form = ActionplanRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'actionplan_register.html')

    return render(request,'actionplan_register.html')



def awarness_register_form(request):
    if request.method == 'POST':
        form = AwarnessRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'awarness_register.html')

    return render(request,'awarness_register.html')


def bp_pulsenote_form(request):
    if request.method == 'POST':
        form = BpPulsenoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'bp_pulsenote.html')

    return render(request,'bp_pulsenote.html')


def counselling_register_form(request):
    if request.method == 'POST':
        form = CounsellingRegisterForm()
        if form.is_valid():
            form.save()
            return redirect(request,'counselling_register.html')

    return render(request,'counselling_register.html')


def medical_camp_form(request):
    if request.method == 'POST':
        form = MedicalCampForm()
        if form.is_valid():
            form.save()
            return redirect(request,'medical_camp.html')

    return render(request,'medical_camp.html')

def medicine_form(request):
    if request.method == 'POST':
        form = MedicineForm()
        if form.is_valid():
            form.save()
            return redirect(request,'medicine.html')

    return render(request,'medicine.html')


def night_survey_form(request):
    if request.method == 'POST':
        form = NightSurveyForm()
        if form.is_valid():
            form.is_valid()
            return redirect(request,'night_survey.html')

    return render(request,'night_survey.html')


def skill_training_form(request):
    if request.method == 'POST':
        form = SkillTrainingForm()
        if form.is_valid():
            form.save()
            return redirect(request,'skill_training.html')

    return render(request,'skill_training.html')


def smc_register_form(request):
    if request.method == 'POST':
        form = SmcRegisterForm()
        if form.is_valid():
            form.save()
            return redirect(request,'smc_register.html')

    return render(request,'smc_register.html')

def staff_attendence_form(request):
    if request.method == 'POST':
        form = StaffAttendenceForm()
        if form.is_valid():
            form.save()
            return redirect(request,'staff_attendence.html')

    return render(request,'staff_attendence.html')


def stock_form(request):
    if request.method == 'POST':
        form = StockForm()
        if form.is_valid():
            form.save()
            return redirect(request,'stock.html')

    return render(request,'stock.html')


def employment_link_form(request):
    if request.method == 'POST':
        form = EmploymentLinkForm()
        if form.is_valid():
            form.save()
            return redirect(request,'employment_link.html')

    return render(request,'employment_link.html')



def rehabitation_form(request):
    if request.method == 'POST':
        form = RehabitationForm()
        if form.is_valid():
            form.save()
            return redirect(request,'rehabitation.html')

    return render(request,'rehabitation.html')


def death_register_form(request):
    if request.method == 'POST':
        form = DeathRegisterForm()
        if form.is_valid():
            form.save()
            return redirect(request,'death_register.html')

    return render(request,'death_register.html')


def accident_register_form(request):
    if request.method == 'POST':
        form = AccidentRegisterForm()
        if form.is_valid():
            form.save()
            return redirect(request,'accident_register.html')

    return render(request,'accident_register.html')