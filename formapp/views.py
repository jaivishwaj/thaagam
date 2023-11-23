from django.shortcuts import render,redirect
from .forms import ProvisionForm, VisitorRegisterForm,ReintegrationForm,VisitorRegister,PerformanceAppraisal,Resident,SocialEntertainment,CaseHistory,ActionplanRegister,AwarnesRegister,BpPulsenote,CounsellingRegister,Medicine,NightSurvey,SkillTraining,SmcRegister,StaffAttendance,Stock,EmploymentLink,Rehabitation,DeathRegister,AccidentRegister,MedicalCamp,MedicineForm



from .models import MasterRecords,CaseHistory,UserProfile,provision,Reintegration,SalaryRegister,Medicine,MedicalCamp,CounsellingRegister,BpPulsenote,AwarnesRegister,ActionplanRegister,CaseHistory,SocialEntertainment,Resident,PerformanceAppraisal,VisitorRegister,Asset,FoodMenu,StaffMovement,StaffAttendance

from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import UserProfile


import os
from django.conf import settings

from django.urls import reverse



class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Check if the requested path requires authentication
            if request.path_info.startswith('/accident_register_dashboard/'):
                # Redirect to the login page
                return redirect(reverse('login'))  # Replace 'login' with your login URL name

        response = self.get_response(request)
        return response






@login_required(login_url='login')
def master_records_dashboard(request):
    datas = MasterRecords.objects.all()
    return render(request, 'dashboard/master_records_dashboard.html',{'data':datas})


from django.contrib.auth.models import User

def signupuser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password != confirmpassword:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Check if the username already exists
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already exists. Please choose a different one.")
            else:
                # Create the user if the username doesn't exist
                user = User.objects.create_user(username=uname, email=email, password=password)
                user.save()
                return redirect('login')
    else:
        return render(request, 'signup.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists in the signup data
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            # Authentication successful, log in the user
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('master_records_dashboard')
        else:
            # Authentication failed
            return HttpResponse("Username or Password is incorrect.")
    else:
        # If it's not a POST request, render the login form
        return render(request, 'login.html')




def home(request):
    return render(request, 'home.html')

def provision_form(request):
    if request.method == 'POST':
        material_name = request.POST.get('material_name')
        total_quantity = request.POST.get('total_quantity')
        utilized_quantity = request.POST.get('utilized_quantity')
        balance_quantity = request.POST.get('balance_quantity')
        remarks = request.POST.get('remarks')
        data = provision.objects.create(material_name=material_name,
                                        total_quantity=total_quantity,
                                        utilized_quantity=utilized_quantity,
                                        balance_quantity=balance_quantity,
                                        remarks=remarks)
        data.save()
        return redirect('provision_dashboard')

    return render(request,'provision.html')

# def index_dashboard(request):
#     datas = provision.objects.all()
#     return render(request, 'index_dashboard.html',{'data':datas})

def provision_dashboard(request):
    datas = provision.objects.all()
    return render(request, 'dashboard/provision_dashboard.html',{'data':datas})
def accident_register_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        inmate_name = request.POST.get('inmate_name')
        age_gender = request.POST.get('age_gender')
        accident_condition = request.POST.get('accident_condition')
        accident_place = request.POST.get('accident_place')
        signature = request.POST.get('signature')
        data = AccidentRegister.objects.create(date=date, inmate_name=inmate_name, age_gender=age_gender,
                                               accident_condition=accident_condition,
                                               accident_place=accident_place,
                                               signature=signature)
        data.save()

        return redirect('accident_register_dashboard')

    return render(request, 'accident_register.html')



def accident_register_dashboard(request):
    datas = AccidentRegister.objects.all()
    return render(request, 'dashboard/accident_register_dashboard.html',{'data':datas})



def reintegration_form(request):
    if request.method == 'POST':
        admission_no = request.POST.get('admission_no')
        resident_name = request.POST.get('resident_name')
        date_of_joining = request.POST.get('date_of_joining')
        date_of_leaving = request.POST.get('date_of_leaving')
        reason_for_leaving = request.POST.get('reason_for_leaving')
        address = request.POST.get('address')
        follow_up_conduct = request.POST.get('follow_up_conduct')
        follows = request.POST.get('follows')
        staff_event_close = request.POST.get('staff_event_close')


        data = Reintegration.objects.create(
            admission_no=admission_no,
            resident_name=resident_name,
            date_of_joining=date_of_joining,
            date_of_leaving=date_of_leaving,
            reason_for_leaving=reason_for_leaving,
            address=address,
            follow_up_conduct=follow_up_conduct,
            follows=follows,
            staff_event_close=staff_event_close
        )
        data.save()

        return redirect('reintegration_register_dashboard')

    return render(request, 'reintegration.html')

def reintegration_register_dashboard(request):
    datas = Reintegration.objects.all()
    return render(request, 'dashboard/reintegration_register_dashboard.html',{'data':datas})

def visitor_register_form(request):

    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        whom_to_see = request.POST.get('whom_to_see')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')
        signature = request.POST.get('signature')
        phone_number = request.POST.get('phone_number')
        data = VisitorRegister.objects.create(date=date,
                                              name=name,
                                              whom_to_see=whom_to_see,
                                              in_time=in_time, out_time=out_time,
                                              signature=signature,
                                              phone_number=phone_number)
        data.save()
        return redirect('visitor_registration_dashboard')
    return render(request,'visitor_register.html')



def visitor_registration_dashboard(request):
    datas = VisitorRegister.objects.all()
    return render(request, 'dashboard/visitor_registration_dashboard.html',{'data':datas})





def performance_appraisal_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        beginning_children = request.POST.get('beginning_children')
        new_admission = request.POST.get('new_admission')
        total_strength = request.POST.get('total_strength')
        reintegration = request.POST.get('reintegration')
        rehabilitation = request.POST.get('rehabilitation')
        referral = request.POST.get('referral')
        left = request.POST.get('left')
        death = request.POST.get('death')
        end_strength = request.POST.get('end_strength')
        rescue = request.POST.get('rescue')
        data = PerformanceAppraisal.objects.create(date=date, beginning_children=beginning_children,
                                                   new_admission=new_admission, total_strength=total_strength,
                                                   reintegration=reintegration, rehabilitation=rehabilitation,
                                                   referral=referral, left=left, death=death,
                                                   end_strength=end_strength, rescue=rescue)
        data.save()
        return redirect('performance_appraisal_dashboard')

    return render(request,'performance_appraisal.html')

def performance_appraisal_dashboard(request):
    datas = PerformanceAppraisal.objects.all()
    return render(request, 'dashboard/performance_appraisal_dashboard.html',{'data':datas})



def resident_form(request):
    if request.method == 'POST':
        pupilName = request.POST.get('pupilName')
        dob = request.POST.get('dob')
        attendance =request.POST.get('attendance')
        daysPresent = request.POST.get('daysPresent')
        schoolFee = request.POST.get('schoolFee')
        dayOfPayment = request.POST.get('dayOfPayment')

        data = Resident.objects.create(pupilName=pupilName,
                                       dob=dob,
                                       attendance=attendance,
                                       daysPresent=daysPresent,
                                       schoolFee=schoolFee,
                                       dayOfPayment=dayOfPayment)

        data.save()

        return redirect('resident_attendance_form_dashboard')

    return render(request,'resident.html')


def resident_attendance_form_dashboard(request):
    datas = Resident.objects.all()


    return render(request, 'dashboard/resident_attendance_form_dashboard.html',{'data':datas})


def social_entertainment_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        admission = request.POST.get('admission')
        name = request.POST.get('name')
        workDetails = request.POST.get('workDetails')

        # Create a new instance of your model
        datas = SocialEntertainment.objects.create(
            date=date,
            admission=admission,
            name=name,
            workDetails=workDetails
        )

        datas.save()

        return redirect('social_entertainment_form_dashboard')

    return render(request,'social_entertainment.html')

def social_entertainment_form_dashboard(request):
    datas = SocialEntertainment.objects.all()


    return render(request, 'dashboard/social_entertainment_form_dashboard.html',{'data':datas})




def case_history_form(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        religion = request.POST.get('religion')
        maritalStatus = request.POST.get('maritalStatus')
        identificationMark = request.POST.get('identificationMark')
        educationBackground = request.POST.get('educationBackground')
        occupation = request.POST.get('occupation')
        address = request.POST.get('address')
        residentContactNumber = request.POST.get('residentContactNumber')
        relativeOrFriendsContact = request.POST.get('relativeOrFriendsContact')
        idProofAvailable = request.POST.get('idProofAvailable')
        idProofDetails = request.POST.get('idProofDetails')
        policeMemoAvailable = request.POST.get('policeMemoAvailable')
        policeStationDetails = request.POST.get('policeStationDetails')
        uploaded_file = request.FILES.get('photo')

        if uploaded_file:
            # Save photo to directory
            filename = f'{name}.jpg'
            photos_dir = os.path.join(settings.MEDIA_ROOT, 'photos')

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)


            relative_file_path = os.path.join('photos', filename)

            data = CaseHistory.objects.create(
                photo_url=relative_file_path,
                name=name,
                age=age,
                sex=sex,
                religion=religion,
                maritalStatus=maritalStatus,
                identificationMark=identificationMark,
                educationBackground=educationBackground,
                occupation=occupation,
                address=address,
                residentContactNumber=residentContactNumber,
                relativeOrFriendsContact=relativeOrFriendsContact,
                idProofAvailable=idProofAvailable,
                idProofDetails=idProofDetails,
                policeMemoAvailable=policeMemoAvailable,
                policeStationDetails=policeStationDetails
            )

            data.save()

            return redirect('case_history_record_dashboard')

    return render(request, 'case_history.html')

def case_history_record_dashboard(request):
    datas = CaseHistory.objects.all()
    return render(request, 'dashboard/case_history_record_dashboard.html', {'data': datas})








def actionplan_register_form(request):
    if request.method == 'POST':
        date_of_plan = request.POST.get('date_of_plan')
        detailed_notes = request.POST.get('detailed_notes')
        action_plan_date = request.POST.get('action_plan_date')


        data = ActionplanRegister.objects.create(date_of_plan=date_of_plan,
                                                 detailed_notes=detailed_notes,
                                                 action_plan_date=action_plan_date)

        data.save()

        return redirect('action_plan_dashboard')


    return render(request,'actionplan_register.html')

def action_plan_dashboard(request):
    datas = ActionplanRegister.objects.all()
    return render(request, 'dashboard/action_plan_dashboard.html',{'data':datas})




def awarnes_register_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = request.POST.get('place')
        details = request.POST.get('details')
        participants = request.POST.get('participants')


        data = AwarnesRegister.objects.create(date=date,
                                              time=time,
                                              place=place,
                                              details=details,
                                              participants=participants)

        data.save()

        return redirect('awarnes_register_dashboard')


    return render(request,'awarnes_register.html')

def awarnes_register_dashboard(request):
    datas = AwarnesRegister.objects.all()
    return render(request, 'dashboard/awarnes_register_dashboard.html',{'data':datas})


def asset_form(request):
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        date_purchase = request.POST.get('date_purchase')
        name_asset = request.POST.get('name_asset')
        no_of_items = request.POST.get('no_of_items')
        cost = request.POST.get('cost')
        bill_no = request.POST.get('bill_no')
        place_asset = request.POST.get('place_asset')
        owner_asset = request.POST.get('owner_asset')
        dispose_date = request.POST.get('dispose_date')

        data = Asset.objects.create( s_no=s_no,
                                    date_purchase=date_purchase,
                                    name_asset=name_asset,
                                    no_of_items=no_of_items,
                                    cost=cost,
                                    bill_no=bill_no,
                                    place_asset=place_asset,
                                    owner_asset=owner_asset,
                                    dispose_date=dispose_date)

        data.save()

        return redirect('asset_register_dashboard')

    return render(request, 'asset.html')


def asset_register_dashboard(request):
    datas = Asset.objects.all()
    return render(request, 'dashboard/asset_register_dashboard.html',{'data':datas})



def bp_pulsenote(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        pulse = request.POST.get('pulse')
        bp = request.POST.get('bp')
        temperature = request.POST.get('temperature')


        data = BpPulsenote.objects.create(
            date=date,
            sno=sno,
            name=name,
            pulse=pulse,
            bp=bp,
            temperature=temperature
        )

        data.save()

        return redirect('bp_form_dashboard')


    return render(request,'bp_pulsenote.html')

def bp_form_dashboard(request):
    datas = BpPulsenote.objects.all()
    return render(request, 'dashboard/bp_form_dashboard.html',{'data':datas})

def counselling_register_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        number_of_sessions = request.POST.get('number_of_sessions')
        observation_identification = request.POST.get('observation_identification')
        signature = request.POST.get('signature')


        data = CounsellingRegister.objects.create(
            date=date,
            name=name,
            number_of_sessions=number_of_sessions,
            observation_identification=observation_identification,
            signature=signature
        )

        data.save()

        return redirect('counselling_register_dashboard')


    return render(request,'counselling_register.html')

def counselling_register_dashboard(request):
    datas = CounsellingRegister.objects.all()
    return render(request, 'dashboard/counselling_register_dashboard.html',{'data':datas})

def medical_camp_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        place = request.POST.get('place')
        name = request.POST.get('name')
        age = request.POST.get('age')
        complaints = request.POST.get('complaints')
        others = request.POST.get('others')
        treatment = request.POST.get('treatment')

        data = MedicalCamp.objects.create(
            date=date,
            place=place,
            name=name,
            age=age,
            complaints=complaints,
            others=others,
            treatment=treatment)
        data.save()

        return redirect('medical_register_dashboard')


    return render(request, 'medical_camp.html')

def medical_register_dashboard(request):
    datas = MedicalCamp.objects.all()
    return render(request, 'dashboard/medical_register_dashboard.html',{'data':datas})



def medicine_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        type_of_disease = request.POST.get('type_of_disease')
        tablet_details = request.POST.get('tablet_details')
        # morning = request.POST.get('morning')
        # afternoon = request.POST.get('afternoon')
        # night = request.POST.get('night')


        datas = Medicine.objects.create(name=name,
                                        age=age,
                                        type_of_disease=type_of_disease,
                                        tablet_details=tablet_details)
                                        # morning=morning,
                                        # afternoon=afternoon,
                                        # night=night)

        datas.save()

        return redirect('medicine_register_dashboard')


    return render(request,'medicine.html')

def medicine_register_dashboard(request):
    datas = Medicine.objects.all()
    return render(request, 'dashboard/medicine_register_dashboard.html',{'data':datas})



def night_survey_form(request):
     if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = request.POST.get('place')
        details_of_visit = request.POST.get('details_of_visit')
        number_of_rescue = request.POST.get('number_of_rescue')
        datas = NightSurvey.objects.create(date=date,
                                           time=time,
                                           place=place,
                                           details_of_visit=details_of_visit,
                                           number_of_rescue =number_of_rescue)
        datas.save()
        return redirect('night_survey_dashboard')

     return render(request, 'night_survey.html')

def night_survey_dashboard(request):
     datas = NightSurvey.objects.all()
     return render(request, 'dashboard/night_survey_dashboard.html', {'data': datas})




def skill_training_form(request):
    if request.method == 'POST':
        sl_no = request.POST.get('sl_no')
        date = request.POST.get('date')
        resident_name = request.POST.get('resident_name')
        skill_training_details = request.POST.get('skill_training_details')
        datas = SkillTraining.objects.create(sl_no=sl_no,
                                             date=date,
                                             resident_name=resident_name,
                                             skill_training_details=skill_training_details)
        datas.save()
        return redirect('skill_training_dashboard')

    return render(request, 'skill_training.html')

def skill_training_dashboard(request):
    datas = SkillTraining.objects.all()
    return render(request, 'dashboard/skill_training_dashboard.html',{'data':datas})





def smc_register_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        introduction_of_meeting = request.POST.get('introduction_of_meeting')
        last_month_performance_details = request.POST.get('last_month_performance_details')
        issue_resolved = request.POST.get('issue_resolved')
        this_month_issue = request.POST.get('this_month_issue')
        ngo_staff_name = request.POST.get('ngo_staff_name')
        gcc_officials_name = request.POST.get('gcc_officials_name')
        police_officials_name = request.POST.get('police_officials_name')
        residents_name = request.POST.get('residents_name')
        datas = SmcRegister.objects.create(date=date,
                                           time=time,
                                           introduction_of_meeting=introduction_of_meeting,
                                           last_month_performance_details=last_month_performance_details,
                                           issue_resolved=issue_resolved,
                                           this_month_issue=this_month_issue,
                                           ngo_staff_name=ngo_staff_name,
                                           gcc_officials_name=gcc_officials_name,
                                           police_officials_name=police_officials_name,
                                           residents_name=residents_name)
        datas.save()
        return redirect('smc_register_dashboard')

    return render(request, 'smc_register.html')
def smc_register_dashboard(request):
    datas = SmcRegister.objects.all()
    return render(request, 'dashboard/smc_register_dashboard.html',{'data':datas})



def staff_attendance_form(request):
    if request.method == 'POST':
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        working_hours = request.POST.get('working_hours')
        days = request.POST.get('days')
        working_days = request.POST.get('working_days')
        leave_days = request.POST.get('leave_days')

        datas = StaffAttendance.objects.create(sno=sno,
                                               name=name,
                                               designation=designation,
                                               working_hours=working_hours,
                                               days=days, working_days=working_days,
                                               leave_days=leave_days)
        datas.save()
        return redirect('staff_attendance_register_dashboard')

    return render(request, 'staff_attendance.html')



def staff_attendance_register_dashboard(request):
    datas = StaffAttendance.objects.all()
    return render(request, 'dashboard/staff_attendance_register_dashboard.html',{'data':datas})


def stock_form(request):
    if request.method == 'POST':

        date = request.POST.get('date')
        particulars = request.POST.get('particulars')
        receipt = request.POST.get('receipt')
        issued = request.POST.get('issued')
        balance = request.POST.get('balance')
        datas = Stock.objects.create( date=date,
                                      particulars=particulars,
                                      receipt=receipt,
                                      issued=issued,
                                      balance=balance)
        datas.save()
        return redirect('stock_register_dashboard')

    return render(request, 'stock.html')


def stock_register_dashboard(request):
    datas = Stock.objects.all()
    return render(request, 'dashboard/stock_register_dashboard.html',{'data':datas})



def employment_link_form(request):
    if request.method == 'POST':
        si_no = request.POST.get('si_no')
        admission_no = request.POST.get('admission_no')
        admission_date = request.POST.get('admission_date')
        resident_name = request.POST.get('resident_name')
        employment_name = request.POST.get('employment_name')
        address_and_contact_details = request.POST.get('address_and_contact_details')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        signature = request.POST.get('signature')
        datas = EmploymentLink.objects.create(si_no=si_no,
                                     admission_no=admission_no,
                                     admission_date=admission_date,
                                     resident_name=resident_name,
                                     address_and_contact_details=address_and_contact_details,
                                     employment_name = employment_name,
                                     designation=designation,
                                     joining_date=joining_date,
                                     signature=signature)

        datas.save()
        return redirect('employment_linkage_form_dashboard')

    return render(request, 'employment_link.html')
def employment_linkage_form_dashboard(request):
    datas = EmploymentLink.objects.all()
    return render(request, 'dashboard/employment_linkage_form_dashboard.html',{'data':datas})





def rehabitation_form(request):
    if request.method == 'POST':
        sno = request.POST.get('sno')
        admission_number = request.POST.get('admission_number')
        name_of_the_resident = request.POST.get('name_of_the_resident')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        date_of_joining = request.POST.get('date_of_joining')
        date_of_leaving = request.POST.get('date_of_leaving')
        mode_of_rescue = request.POST.get('mode_of_rescue')
        mode_of_rehabilitation = request.POST.get('mode_of_rehabilitation')
        follow_up = request.POST.get('follow_up')
        datas = Rehabitation.objects.create(sno=sno,
                                            admission_number=admission_number,
                                            name_of_the_resident=name_of_the_resident,
                                            age=age,
                                            sex=sex, date_of_joining=date_of_joining,
                                            date_of_leaving=date_of_leaving,
                                            mode_of_rescue=mode_of_rescue,
                                            mode_of_rehabilitation = mode_of_rehabilitation,
                                            follow_up=follow_up)
        datas.save()
        return redirect('rehabitation_dashboard')

    return render(request, 'rehabitation.html')


def rehabitation_dashboard(request):
    datas = Rehabitation.objects.all()
    return render(request, 'dashboard/rehabitation_dashboard.html',{'data':datas})

def death_register_form(request):
    if request.method == 'POST':
        sno = request.POST.get('sno')
        name_of_the_death_person = request.POST.get('name_of_the_death_person')
        age_sex = request.POST.get('age_sex')
        date_of_death = request.POST.get('date_of_death')
        reason_for_death = request.POST.get('reason_for_death')
        whom_to_claim_death_person = request.POST.get('whom_to_claim_death_person')
        address_and_contact_number = request.POST.get('address_and_contact_number')
        legal_producer_taken_if_unclaimed = request.POST.get('legal_producer_taken_if_unclaimed')
        remarks = request.POST.get('remarks')
        datas = DeathRegister.objects.create(sno=sno,
                                             name_of_the_death_person=name_of_the_death_person,
                                             age_sex=age_sex,
                                             date_of_death=date_of_death,
                                             reason_for_death=reason_for_death,
                                             whom_to_claim_death_person=whom_to_claim_death_person,
                                             address_and_contact_number=address_and_contact_number,
                                             legal_producer_taken_if_unclaimed=legal_producer_taken_if_unclaimed,
                                             remarks = remarks)
        datas.save()
        return redirect('death_register_dashboard')

    return render(request,'death_register.html')

def death_register_dashboard(request):
    datas = DeathRegister.objects.all()
    return render(request, 'dashboard/death_register_dashboard.html',{'data':datas})


def food_menu_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        morning_snacks = request.POST.get('morning_snacks')
        no_of_resident1 = request.POST.get('no_of_resident1')
        breakfast = request.POST.get('breakfast')
        no_of_resident2 = request.POST.get('no_of_resident2')
        lunch = request.POST.get('lunch')
        no_of_resident3 = request.POST.get('no_of_resident3')
        dinner = request.POST.get('dinner')
        no_of_resident4 = request.POST.get('no_of_resident4')

        data = FoodMenu(date=date,
                        morning_snacks=morning_snacks,
                        no_of_resident1=no_of_resident1,
                        breakfast=breakfast,
                        no_of_resident2=no_of_resident2,
                        lunch=lunch,
                        no_of_resident3=no_of_resident3,
                        dinner=dinner,
                        no_of_resident4=no_of_resident4)
        data.save()
        return redirect('food_menu_dashboard')
    return render(request, 'food_menu.html')

def food_menu_dashboard(request):
    datas = FoodMenu.objects.all()
    return render(request, 'dashboard/food_menu_dashboard.html',{'data':datas})



def salary_register_form(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        sign = request.POST.get('sign')

        data = SalaryRegister(date=date,
                              name=name,
                              designation=designation,
                              salary=salary,
                              sign=sign)

        data.save()
        return redirect('salary_register_dashboard')
    return render(request, 'salary_register.html')

def salary_register_dashboard(request):
    datas = SalaryRegister.objects.all()
    return render(request, 'dashboard/salary_register_dashboard.html',{'data':datas})


def staff_movement_form(request):
    if request.method == 'POST':
          date_of_plan = request.POST.get('date_of_plan')
          working_area = request.POST.get('Working_Area')
          nature_of_work = request.POST.get('Nature_of_Work')
          work_done_by = request.POST.get('Work_done_By')
          sign = request.POST.get('Sign')

          data = StaffMovement(date_of_plan=date_of_plan,
                               working_area=working_area,
                               nature_of_work=nature_of_work,
                               work_done_by=work_done_by,
                               sign=sign)

          data.save()

          return redirect('staff_movement_note_dashboard')
    return render(request, "staff_movement.html")


def staff_movement_note_dashboard(request):
    datas = StaffMovement.objects.all()
    return render(request, 'dashboard/staff_movement_note_dashboard.html',{'data':datas})



def master_records_form(request):
    if request.method == 'POST':
        S_no = request.POST.get('S_no')
        name = request.POST.get('name')
        Aid_no = request.POST.get('Aid_no')
        Age_gender = request.POST.get('Age_gender')
        dob = request.POST.get('dob')
        Date_Of_Admission = request.POST.get('Date_Of_Admission')
        Date_Of_Leaving = request.POST.get('Date_Of_Leaving')
        Family_Contact_No = request.POST.get('Family_Contact_No')
        Relation = request.POST.get('Relation')
        Permanent_Address = request.POST.get('Permanent_Address')
        Mode_Of_Identification_Rescue = request.POST.get('Mode_Of_Identification_Rescue')
        Identification_Mark = request.POST.get('Identification_Mark')
        Identification_Papers = request.POST.get('Identification_Papers')
        Rehabilitation_Measures = request.POST.get('Rehabilitation_Measures')
        Reason_For_Leaving_Shelter = request.POST.get('Reason_For_Leaving_Shelter')
        Follow_Up_Action = request.POST.get('Follow_Up_Action')
        Second_Follow_Up = request.POST.get('Second_Follow_Up')
        Medical_Status = request.POST.get('Medical_Status')
        File_Closure_Status = request.POST.get('File_Closure_Status')
        Remarks = request.POST.get('Remarks')
        Signature = request.POST.get('Signature')
        uploaded_file = request.FILES.get('photo')

        if uploaded_file:
            # Save photo to directory
            filename = f'{name}.jpg'
            photos_dir = os.path.join(settings.MEDIA_ROOT, 'photos')

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            relative_file_path = os.path.join('photos', filename)


        data = MasterRecords(

            S_no=S_no,
            name=name,
            Aid_no=Aid_no,
            Age_gender=Age_gender,
            dob=dob,
            Date_Of_Admission=Date_Of_Admission,
            Date_Of_Leaving=Date_Of_Leaving,
            Family_Contact_No=Family_Contact_No,
            Relation=Relation,
            Permanent_Address=Permanent_Address,
            Mode_Of_Identification_Rescue=Mode_Of_Identification_Rescue,
            Identification_Mark=Identification_Mark,
            Identification_Papers=Identification_Papers,
            Rehabilitation_Measures=Rehabilitation_Measures,
            Reason_For_Leaving_Shelter=Reason_For_Leaving_Shelter,
            Follow_Up_Action=Follow_Up_Action,
            Second_Follow_Up=Second_Follow_Up,
            Medical_Status=Medical_Status,
            File_Closure_Status=File_Closure_Status,
            Remarks=Remarks,
            Signature=Signature,
            photo_url = relative_file_path
        )
        data.save()
        return redirect('master_records_dashboard')

    return render(request, 'master_records.html')



def master_records_dashboard(request):
    datas = MasterRecords.objects.all()
    return render(request, 'dashboard/master_records_dashboard.html',{'data':datas})




@login_required(login_url='login')
def restricted_page(request):
    return render(request, 'restricted_page.html')
