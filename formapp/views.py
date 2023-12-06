from django.shortcuts import render, redirect

# from .forms import ProvisionForm, VisitorRegisterForm,ReintegrationForm,VisitorRegister,PerformanceAppraisal,Resident,SocialEntertainment,CaseHistory,ActionplanRegister,AwarnesRegister,BpPulsenote,CounsellingRegister,Medicine,NightSurvey,SkillTraining,SmcRegister,StaffAttendance,Stock,EmploymentLink,Rehabitation,DeathRegister,AccidentRegister,MedicalCamp,MedicineForm


from .models import (
    Inspectionregister,
    MasterRecords,
    CaseHistory,

    provision,
    Reintegration,
    SalaryRegister,
    Medicine,
    MedicalCamp,
    CounsellingRegister,
    BpPulsenote,
    AwarnesRegister,
    ActionplanRegister,

    SocialEntertainment,
    Resident,
    PerformanceAppraisal,
    VisitorRegister,
    Asset,
    FoodMenu,
    StaffMovement,
    StaffAttendance,
    PersonalInfo,
    AccidentRegister,
    Stock,
    EmploymentLink,
    Rehabitation,
    DeathRegister,
    NightSurvey,
    SkillTraining,
    SmcRegister,
)


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import userprofile
import os
from django.conf import settings

from django.urls import reverse

from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import provision

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
# from .models import userprofile


def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        confrimpassword = request.POST.get('confrimpassword')

        User = get_user_model()  # Get the custom user model
        if not User.objects.filter(username=username).exists():
            # Create a new user instance and set the username
            user = User.objects.create_user(username=username, password=password)
            Userprofile=userprofile.objects.create(username=username, email=email, password=password, mobile_number=mobile_number,confrimpassword=confrimpassword)
            # Save the user
            Userprofile.save()
            user.save()
            return redirect('login')  # Redirect to login upon successful registration
        else:
            # Authentication failed, handle accordingly (e.g., display an error message)

            return redirect('signup')

    return render(request, 'signup.html')

from django.contrib.auth import authenticate,login

#----------------------------------------------------------!-------------------------------------------------------------
# def loginuser(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             # Sign in user with Firebase authentication
#             login = auth.sign_in_with_email_and_password(email, password)
#             print("Successfully logged in")
#             user = authenticate(request, email=email, password=password)
#             # Retrieve user data from Firebase if needed
#             user_info = auth.get_account_info(login['idToken'])
#
#             # Instead of creating a new user profile on every login, retrieve or update existing profile if needed
#             user_profile, created = userprofile.objects.get_or_create(email=email, password=password)
#             # Update user profile data if needed
#             # user_profile.some_field = some_value
#             # user_profile.save()
#
#             return redirect('home')
#         except:
#
#             return redirect('loginfails')
#     return render(request, 'login.html')
#----------------------------------------------------------^-------------------------------------------------------------
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Assuming 'username' is the field name
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful, log the user in
            login(request, user)
            # You can perform additional actions after login if needed
            request.session['user'] = user.username  # Storing username in session
            return redirect('home')  # Redirect to a success page (replace 'sr' with your URL name)
        else:
            # Authentication failed, handle accordingly (e.g., display an error message)

            return redirect('signup')

    return render(request, 'login.html')

#========================================================!===============================================================

def logout_view(request):
    request.session.flush()
    return redirect("login")


# def home(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     # if request.user.is_authenticated:
#     #     return render(request, 'home.html')
#     else:
#         return redirect('login')





def home(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    return render(request, "home.html",{'user': user})


# @login_required(login_url='login')
def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        confrimpassword = request.POST.get('confrimpassword')

        User = get_user_model()  # Get the custom user model
        if not User.objects.filter(username=username).exists():
            # Create a new user instance and set the username
            user = User.objects.create_user(username=username, password=password)
            Userprofile=userprofile.objects.create(username=username, email=email, password=password, mobile_number=mobile_number,confrimpassword=confrimpassword)
            # Save the user
            Userprofile.save()
            user.save()
            return redirect('login')  # Redirect to login upon successful registration
        else:
            # Authentication failed, handle accordingly (e.g., display an error message)

            return redirect('signup')

    return render(request, 'signup.html')

from django.contrib.auth import authenticate,login



def accident_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        date = request.POST.get("date")
        inmate_name = request.POST.get("inmate_name")
        age_gender = request.POST.get("age_gender")
        accident_condition = request.POST.get("accident_condition")
        accident_place = request.POST.get("accident_place")
        signature = request.POST.get("signature")
        data = AccidentRegister.objects.create(uqid=uqid,
            date=date,
            inmate_name=inmate_name,
            age_gender=age_gender,
            accident_condition=accident_condition,
            accident_place=accident_place,
            signature=signature,
        )
        data.save()
        return redirect("accident_register_dashboard")
    return render(request, "accident_register.html",{'user': user})



def accident_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
       return redirect("login")
    datas = AccidentRegister.objects.all()
    return render(
        request, "dashboard/accident_register_dashboard.html", {"data": datas})


def reintegration_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        admission_no = request.POST.get("admission_no")
        uqid = request.POST.get("uqid")
        resident_name = request.POST.get("resident_name")
        date_of_joining = request.POST.get("date_of_joining")
        date_of_leaving = request.POST.get("date_of_leaving")
        reason_for_leaving = request.POST.get("reason_for_leaving")
        address = request.POST.get("address")
        follow_up_conduct = request.POST.get("follow_up_conduct")
        follows = request.POST.get("follows")
        staff_event_close = request.POST.get("staff_event_close")

        data = Reintegration.objects.create(
            admission_no=admission_no,
            uqid=uqid,
            resident_name=resident_name,
            date_of_joining=date_of_joining,
            date_of_leaving=date_of_leaving,
            reason_for_leaving=reason_for_leaving,
            address=address,
            follow_up_conduct=follow_up_conduct,
            follows=follows,
            staff_event_close=staff_event_close,
        )
        data.save()

        return redirect("reintegration_register_dashboard")

    return render(request, "reintegration_register.html",{'user': user})


def reintegration_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Reintegration.objects.all()
     return render(
        request, "dashboard/reintegration_register_dashboard.html", {"data": datas}
    )

def visitor_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']

    if request.method == "POST":
        date = request.POST.get("date")
        name = request.POST.get("name")
        uqid = request.POST.get("uqid")
        whom_to_see = request.POST.get("whom_to_see")
        in_time = request.POST.get("in_time")
        out_time = request.POST.get("out_time")
        phone_number = request.POST.get("phone_number")
        signature = request.POST.get("signature")
        data = VisitorRegister.objects.create(
            date=date,
            uqid=uqid,
            name=name,
            whom_to_see=whom_to_see,
            in_time=in_time,
            out_time=out_time,
            phone_number=phone_number,
            signature=signature,
        )
        data.save()
        return redirect("visitor_registration_dashboard")
    return render(request, "visitor_registration.html",{'user': user})


def visitor_registration_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = VisitorRegister.objects.all()
     return render(
        request, "dashboard/visitor_registration_dashboard.html", {"data": datas}
    )


def performance_appraisal_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        beginning_children = request.POST.get("beginning_children")
        new_admission = request.POST.get("new_admission")
        total_strength = request.POST.get("total_strength")
        reintegration = request.POST.get("reintegration")
        rehabilitation = request.POST.get("rehabilitation")
        referral = request.POST.get("referral")
        left = request.POST.get("left")
        death = request.POST.get("death")
        end_strength = request.POST.get("end_strength")
        rescue = request.POST.get("rescue")

        data = PerformanceAppraisal.objects.create(
            date=date,
            uqid=uqid,
            beginning_children=beginning_children,
            new_admission=new_admission,
            total_strength=total_strength,
            reintegration=reintegration,
            rehabilitation=rehabilitation,
            referral=referral,
            left=left,
            death=death,
            end_strength=end_strength,
            rescue=rescue,
        )
        data.save()
        return redirect("performance_appraisal_dashboard")  # Redirect to appropriate page after form submission

    return render(request, "performance_appraisal.html",{'user': user})


def performance_appraisal_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = PerformanceAppraisal.objects.all()
     return render(
        request, "dashboard/performance_appraisal_dashboard.html", {"data": datas})


def resident_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        pupilName = request.POST.get("name_pupil")
        uqid = request.POST.get("uqid")
        dob = request.POST.get("dob")
        attendance = request.POST.get("attendance")
        daysPresent = request.POST.get("daysPresent")
        schoolFee = request.POST.get("schoolFee")
        dayOfPayment = request.POST.get("dayOfPayment")

        data = Resident.objects.create(
            pupilName=pupilName,
            dob=dob,uqid=uqid,
            attendance=attendance,
            daysPresent=daysPresent,
            schoolFee=schoolFee,
            dayOfPayment=dayOfPayment,
        )

        data.save()

        return redirect("resident_attendance_form_dashboard")

    return render(request, "resident_attendance.html",{'user': user})


def resident_attendance_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Resident.objects.all()
     return render(
        request, "dashboard/resident_attendance_form_dashboard.html", {"data": datas}
    )


def social_entertainment_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        admission = request.POST.get("admission")
        name = request.POST.get("name")
        workDetails = request.POST.get("workDetails")

        # Create a new instance of your model
        data = SocialEntertainment.objects.create(
            date=date,uqid=uqid, admission=admission, name=name, workDetails=workDetails
        )

        data.save()

        return redirect("social_entertainment_form_dashboard")

    return render(request, "social_entertainment_record.html",{'user': user})


def social_entertainment_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = SocialEntertainment.objects.all()
     return render(
        request, "dashboard/social_entertainment_form_dashboard.html", {"data": datas})


def inspection_register(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        # Get data from the form
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        message = request.POST.get("message")
        date = request.POST.get("date")
        time = request.POST.get("time")
        sign = request.POST.get("sign")

        # Create an instance of the model and save data
        data = Inspectionregister.objects.create(

            designation=designation,
            name=name,
            message=message,
            date=date,
            time=time,
            sign=sign,
        )
        data.save()

        # Redirect after successful submission (optional)
        return redirect("inspection_register_dashboard")

    return render(request, "inspection_register.html",{'user': user})


def inspection_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Inspectionregister.objects.all()
     return render(
        request, "dashboard/inspection_records_dashboard.html", {"data": datas})


def case_history_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        form_data = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "sex": request.POST.get("sex"),
            "uqid": request.POST.get("uqid"),
            "religion": request.POST.get("religion"),
            "maritalStatus": request.POST.get("maritalStatus"),
            "identificationMark": request.POST.get("identificationMark"),
            "educationBackground": request.POST.get("educationBackground"),
            "occupation": request.POST.get("occupation"),
            "address": request.POST.get("address"),
            "residentContactNumber": request.POST.get("residentContactNumber"),
            "relativeOrFriendsContact": request.POST.get("relativeOrFriendsContact"),
            "idProofAvailable": request.POST.get("idProofAvailable"),
            "idProofDetails": request.POST.get("idProofDetails"),
            "policeMemoAvailable": request.POST.get("policeMemoAvailable"),
            "policeStationDetails": request.POST.get("policeStationDetails"),
            "uploaded_file": request.FILES.get("photo"),
        }

        # Implement form validation here

        if form_data["uploaded_file"]:
            # Securely handle file upload
            filename = f"{form_data['name']}.jpg"
            photos_dir = os.path.join(settings.MEDIA_ROOT, "photos")

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, "wb") as destination:
                for chunk in form_data["uploaded_file"].chunks():
                    destination.write(chunk)

            relative_file_path = os.path.join("photos", filename)

            # Create CaseHistory object and save data
            data = CaseHistory(
                photo_url=relative_file_path,
                **{k: v for k, v in form_data.items() if k != "uploaded_file"}
            )
            data.save()

            return redirect("case_history_record_dashboard")

    return render(request, "case_history.html",{'user': user})

def case_history_record_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = CaseHistory.objects.all()
     return render(request, "dashboard/case_history_record_dashboard.html",{"data": datas})

def personal_info_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        date = request.POST.get("date")
        street_address = request.POST.get("street_address")
        street_address2 = request.POST.get("street_address_2")
        state = request.POST.get("state")
        city = request.POST.get("city")

        postal = request.POST.get("postal_code")
        phone_number = request.POST.get("phone_number")
        home_phone_number = request.POST.get("home_phone_number")
        email = request.POST.get("email")
        birthdate = request.POST.get("birthdate")
        uploadfile = request.FILES.get("upload_file")

        if uploadfile:
            # Save photo to directory
            filename = f"{name}.jpg"
            photos_dir = os.path.join(settings.MEDIA_ROOT, "photos")

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, "wb") as destination:
                for chunk in uploadfile.chunks():
                    destination.write(chunk)

            relative_file_path = os.path.join("photos", filename)

            data = PersonalInfo.objects.create(
                photo_url=relative_file_path,
                uqid=uqid,
                name=name,
                date=date,
                street_address=street_address,
                street_address_2=street_address2,  # Update field name
                city=city,
                state_province=state,  # Update field name
                postal_code=postal,  # Update field name
                phone_number=phone_number,
                home_phone_number=home_phone_number,
                email=email,
                birthdate=birthdate,
            )

            data.save()
            return redirect("personal_info_dashboard")

    return render(request, "personal_information.html",{'user': user})


def personal_info_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = PersonalInfo.objects.all()
     return render(
        request, "dashboard/personal_information_dashboard.html",{"data": datas})


def actionplan_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date_of_plan = request.POST.get("date_of_plan")
        detailed_notes = request.POST.get("detailed_notes")
        action_plan_date = request.POST.get("action_plan_date")

        data = ActionplanRegister.objects.create(
            date_of_plan=date_of_plan,
            detailed_notes=detailed_notes,
            action_plan_date=action_plan_date,
        )

        data.save()

        return redirect("action_plan_dashboard")

    return render(request, "actionplan_register.html",{'user': user})


def action_plan_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = ActionplanRegister.objects.all()
     return render(request, "dashboard/action_plan_dashboard.html",{"data": datas})


def awarnes_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        place = request.POST.get("place")
        details = request.POST.get("details")
        participants = request.POST.get("participants")

        data = AwarnesRegister.objects.create(
            date=date,
            time=time,
            place=place,
            details=details,
            participants=participants,
        )

        data.save()

        return redirect("awarnes_register_dashboard")

    return render(request, "awarnes_register.html",{'user': user})


def awarnes_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = AwarnesRegister.objects.all()
     return render(request, "dashboard/awarnes_register_dashboard.html",{"data": datas})


def asset_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        date_purchase = request.POST.get("date_purchase")
        name_asset = request.POST.get("name_asset")
        no_of_items = request.POST.get("no_of_items")
        cost = request.POST.get("cost")
        bill_no = request.POST.get("bill_no")
        place_asset = request.POST.get("place_asset")
        owner_asset = request.POST.get("owner_asset")
        dispose_date = request.POST.get("dispose_date")

        data = Asset.objects.create(
            uqid=uqid,
            date_purchase=date_purchase,
            name_asset=name_asset,
            no_of_items=no_of_items,
            cost=cost,
            bill_no=bill_no,
            place_asset=place_asset,
            owner_asset=owner_asset,
            dispose_date=dispose_date,
        )

        data.save()

        return redirect("asset_register_dashboard")

    return render(request, "asset.html",{'user': user})
def asset_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Asset.objects.all()
     return render(request, "dashboard/asset_register_dashboard.html",{"data": datas})


def bp_pulsenote(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        pulse = request.POST.get("pulse")
        bp = request.POST.get("bp")
        temperature = request.POST.get("temperature")

        data = BpPulsenote.objects.create(
            date=date, uqid=uqid, name=name, pulse=pulse, bp=bp, temperature=temperature
        )

        data.save()

        return redirect("bp_form_dashboard")

    return render(request, "bp_pulsenote.html",{'user': user})


def bp_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = BpPulsenote.objects.all()
     return render(request, "dashboard/bp_form_dashboard.html",{"data": datas})


def counselling_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        number_of_sessions = request.POST.get("number_of_sessions")
        observation_identification = request.POST.get("observation_identification")
        signature = request.POST.get("signature")

        data = CounsellingRegister.objects.create(
            date=date,
            uqid=uqid,
            name=name,
            number_of_sessions=number_of_sessions,
            observation_identification=observation_identification,
            signature=signature,
        )

        data.save()

        return redirect("counselling_register_dashboard")

    return render(request, "counselling_register.html",{'user': user})



def counselling_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = CounsellingRegister.objects.all()
     return render(request, "dashboard/counselling_register_dashboard.html", {"data": datas})


def medical_camp_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        place = request.POST.get("place")
        name = request.POST.get("name")
        age = request.POST.get("age")
        complaints = request.POST.get("complaints")
        others = request.POST.get("others")
        treatment = request.POST.get("treatment")

        data = MedicalCamp.objects.create(
            date=date,
            uqid=uqid,
            place=place,
            name=name,
            age=age,
            complaints=complaints,
            others=others,
            treatment=treatment,
        )
        data.save()

        return redirect("medical_register_dashboard")

    return render(request, "medical_camp.html",{'user': user})


def medical_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = MedicalCamp.objects.all()
     return render(request, "dashboard/medical_register_dashboard.html",{"data": datas})


def medicine_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        name = request.POST.get("name")
        uqid = request.POST.get("uqid")
        age = request.POST.get("age")
        type_of_disease = request.POST.get("type_of_disease")
        tablet_details = request.POST.get("tablet_details")
        # morning = request.POST.get('morning')
        # afternoon = request.POST.get('afternoon')
        # night = request.POST.get('night')

        datas = Medicine.objects.create(uqid=uqid,
            name=name,
            age=age,
            type_of_disease=type_of_disease,
            tablet_details=tablet_details,
        )
        # morning=morning,
        # afternoon=afternoon,
        # night=night)

        datas.save()

        return redirect("medicine_register_dashboard")

    return render(request, "medicine.html",{'user': user})


def medicine_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Medicine.objects.all()
     return render(request, "dashboard/medicine_register_dashboard.html",{"data": datas})


def night_survey_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        time = request.POST.get("time")
        place = request.POST.get("place")
        details_of_visit = request.POST.get("details_of_visit")
        number_of_rescue = request.POST.get("number_of_rescue")
        data = NightSurvey.objects.create(
            date=date,
            uqid=uqid,
            time=time,
            place=place,
            details_of_visit=details_of_visit,
            number_of_rescue=number_of_rescue,
        )
        data.save()
        return redirect("night_survey_dashboard")

    return render(request, "night_survey.html",{'user': user})


def night_survey_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = NightSurvey.objects.all()
     return render(request, "dashboard/night_survey_dashboard.html",{"data": datas})


def skill_training_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        date = request.POST.get("date")
        resident_name = request.POST.get("resident_name")
        skill_training_details = request.POST.get("skill_training_details")
        datas = SkillTraining.objects.create(
            uqid=uqid,
            date=date,
            resident_name=resident_name,
            skill_training_details=skill_training_details,
        )
        datas.save()
        return redirect("skill_training_dashboard")

    return render(request, "skill_training.html",{'user': user})


def skill_training_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = SkillTraining.objects.all()
     return render(request, "dashboard/skill_training_dashboard.html",{"data": datas})


def smc_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        introduction_of_meeting = request.POST.get("introduction_of_meeting")
        last_month_performance_details = request.POST.get(
            "last_month_performance_details"
        )
        issue_resolved = request.POST.get("issue_resolved")
        this_month_issue = request.POST.get("this_month_issue")
        ngo_staff_name = request.POST.get("ngo_staff_name")
        gcc_officials_name = request.POST.get("gcc_officials_name")
        police_officials_name = request.POST.get("police_officials_name")
        residents_name = request.POST.get("residents_name")
        datas = SmcRegister.objects.create(
            date=date,
            time=time,
            introduction_of_meeting=introduction_of_meeting,
            last_month_performance_details=last_month_performance_details,
            issue_resolved=issue_resolved,
            this_month_issue=this_month_issue,
            ngo_staff_name=ngo_staff_name,
            gcc_officials_name=gcc_officials_name,
            police_officials_name=police_officials_name,
            residents_name=residents_name,
        )
        datas.save()
        return redirect("smc_register_dashboard")

    return render(request, "smc_register.html",{'user': user})


def smc_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = SmcRegister.objects.all()
     return render(request, "dashboard/smc_register_dashboard.html",{"data": datas})


def staff_attendance_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        working_hours = request.POST.get("working_hours")
        days = request.POST.get("days")
        working_days = request.POST.get("working_days")
        leave_days = request.POST.get("leave_days")
        remarks = request.POST.get("remarks")

        # if (
        #     sno
        #     and name
        #     and designation
        #     and working_hours
        #     and days
        #     and working_days
        #     and leave_days
        #     and remarks
        # ):
            # Create StaffAttendance object
        datas = StaffAttendance.objects.create(
            uqid=uqid,
            name=name,
            designation=designation,
            working_hours=working_hours,
            days=days,
            working_days=working_days,
            leave_days=leave_days,
            remarks = remarks,
        )
        datas.save()
        # No need to call datas.save() again; create() saves the object
        return redirect("staff_attendance_register_dashboard")
    else:
            # Handle invalid or missing data here
            # You can render the form again with an error message
      error_message = "Some data is missing. Please fill in all fields."
      return redirect( "staff_attendance_form",{"error_message": error_message})
    return render(request, "staff_attendance.html",{'user': user})


def staff_attendance_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
      datas = StaffAttendance.objects.all()
      return render(
          request, "dashboard/staff_attendance_register_dashboard.html", {"data": datas})


def stock_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        particulars = request.POST.get("particulars")
        receipt = request.POST.get("receipt")
        issued = request.POST.get("issued")
        balance = request.POST.get("balance")
        datas = Stock.objects.create(
            date=date,
            uqid=uqid,
            particulars=particulars,
            receipt=receipt,
            issued=issued,
            balance=balance,
        )
        datas.save()
        return redirect("stock_register_dashboard")

    return render(request, "stock_register.html",{'user': user})


def stock_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Stock.objects.all()
     return render(request, "dashboard/stock_register_dashboard.html",{"data": datas})


def employment_link_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        admission_no = request.POST.get("admission_no")
        admission_date = request.POST.get("admission_date")
        resident_name = request.POST.get("resident_name")
        employment_name = request.POST.get("employment_name")
        address_and_contact_details = request.POST.get("address_and_contact_details")
        designation = request.POST.get("designation")
        joining_date = request.POST.get("joining_date")
        signature = request.POST.get("signature")
        datas = EmploymentLink.objects.create(
            uqid=uqid,
            admission_no=admission_no,
            admission_date=admission_date,
            resident_name=resident_name,
            address_and_contact_details=address_and_contact_details,
            employment_name=employment_name,
            designation=designation,
            joining_date=joining_date,
            signature=signature,
        )

        datas.save()
        return redirect("employment_linkage_form_dashboard")

    return render(request, "employment_link.html",{'user': user})


def employment_linkage_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
      datas = EmploymentLink.objects.all()
      return render( request, "dashboard/employment_linkage_form_dashboard.html",{"data": datas})


def rehabitation_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        admission_number = request.POST.get("admission_number")
        name_of_the_resident = request.POST.get("name_of_the_resident")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        date_of_joining = request.POST.get("date_of_joining")
        date_of_leaving = request.POST.get("date_of_leaving")
        mode_of_rescue = request.POST.get("mode_of_rescue")
        mode_of_rehabilitation = request.POST.get("mode_of_rehabilitation")
        follow_up = request.POST.get("follow_up")
        datas = Rehabitation.objects.create(
            uqid=uqid,
            admission_number=admission_number,
            name_of_the_resident=name_of_the_resident,
            age=age,
            sex=sex,
            date_of_joining=date_of_joining,
            date_of_leaving=date_of_leaving,
            mode_of_rescue=mode_of_rescue,
            mode_of_rehabilitation=mode_of_rehabilitation,
            follow_up=follow_up,
        )
        datas.save()
        return redirect("rehabitation_dashboard")

    return render(request, "rehabitation.html",{'user': user})


def rehabitation_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = Rehabitation.objects.all()
     return render(request, "dashboard/rehabitation_dashboard.html",{"data": datas})


def death_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        name_of_the_death_person = request.POST.get("name_of_the_death_person")
        date_of_death = request.POST.get("date_of_death")
        reason_for_death = request.POST.get("reason_for_death")
        whom_to_claim_death_person = request.POST.get("whom_to_claim_death_person")
        address_and_contact_number = request.POST.get("address_and_contact_number")
        legal_producer_taken_if_unclaimed = request.POST.get(
            "legal_producer_taken_if_unclaimed"
        )
        remarks = request.POST.get("remarks")

        data = DeathRegister.objects.create(
            uqid=uqid,
            name_of_the_death_person=name_of_the_death_person,
            date_of_death=date_of_death,
            reason_for_death=reason_for_death,
            whom_to_claim_death_person=whom_to_claim_death_person,
            address_and_contact_number=address_and_contact_number,
            legal_producer_taken_if_unclaimed=legal_producer_taken_if_unclaimed,
            remarks=remarks,
        )
        data.save()
        return redirect("death_register_dashboard")

    return render(request, "death_register.html",{'user': user})


def death_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = DeathRegister.objects.all()
     return render(request, "dashboard/death_register_dashboard.html", {"data": datas})


def food_menu_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        morning_snacks = request.POST.get("morning_snacks")
        no_of_resident1 = request.POST.get("no_of_resident1")
        breakfast = request.POST.get("breakfast")
        no_of_resident2 = request.POST.get("no_of_resident2")
        lunch = request.POST.get("lunch")
        no_of_resident3 = request.POST.get("no_of_resident3")
        dinner = request.POST.get("dinner")
        no_of_resident4 = request.POST.get("no_of_resident4")

        data = FoodMenu(
            date=date,
            morning_snacks=morning_snacks,
            no_of_resident1=no_of_resident1,
            breakfast=breakfast,
            no_of_resident2=no_of_resident2,
            lunch=lunch,
            no_of_resident3=no_of_resident3,
            dinner=dinner,
            no_of_resident4=no_of_resident4,
        )
        data.save()
        return redirect("food_menu_dashboard")
    return render(request, "food_menu.html",{'user': user})


def food_menu_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
       datas = FoodMenu.objects.all()
       return render(request, "dashboard/food_menu_dashboard.html", {"data": datas})


def salary_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        salary = request.POST.get("salary")
        sign = request.POST.get("sign")

        data = SalaryRegister(
            date=date,uqid=uqid, name=name, designation=designation, salary=salary, sign=sign
        )

        data.save()
        return redirect("salary_register_dashboard")
    return render(request, "salary_register.html",{'user': user})


def salary_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
       datas = SalaryRegister.objects.all()
       return render(request, "dashboard/salary_register_dashboard.html",{"data": datas})


def staff_movement_form(request):
        user = None
        if 'user' in request.session:
            user = request.session['user']
        if request.method == "POST":
              date_of_plan = request.POST.get("date")
              uqid = request.POST.get("uqid")
              working_area = request.POST.get("Working_Area")
              nature_of_work = request.POST.get("Nature_of_Work")
              work_done_by = request.POST.get("Work_done_By")
              sign = request.POST.get("Sign")

              data = StaffMovement(
                  date_of_plan=date_of_plan,
                  uqid=uqid,
                  working_area=working_area,
                  nature_of_work=nature_of_work,
                  work_done_by=work_done_by,
                  sign=sign,
              )
              data.save()

              return redirect("staff_movement_note_dashboard")
        return render(request, "staff_movement_note.html",{'user': user})

# @login_required(login_url='/login/')
def staff_movement_note_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     datas = StaffMovement.objects.all()
     return render(request, "dashboard/staff_movement_note_dashboard.html",{"data": datas})


def master_records_form(request):
          user = None
          if 'user' in request.session:
             user = request.session['user']
          if request.method == "POST":
              uqid = request.POST.get("uqid")
              name = request.POST.get("name")
              Aid_no = request.POST.get("Aid_no")
              Age_gender = request.POST.get("Age_gender")
              dob = request.POST.get("dob")
              Date_Of_Admission = request.POST.get("Date_Of_Admission")
              Date_Of_Leaving = request.POST.get("Date_Of_Leaving")
              Family_Contact_No = request.POST.get("Family_Contact_No")
              Relation = request.POST.get("Relation")
              Permanent_Address = request.POST.get("Permanent_Address")
              Mode_Of_Identification_Rescue = request.POST.get(
                  "Mode_Of_Identification_Rescue"
              )
              Identification_Mark = request.POST.get("Identification_Mark")
              Identification_Papers = request.POST.get("Identification_Papers")
              Rehabilitation_Measures = request.POST.get("Rehabilitation_Measures")
              Reason_For_Leaving_Shelter = request.POST.get("Reason_For_Leaving_Shelter")
              Follow_Up_Action = request.POST.get("Follow_Up_Action")
              Second_Follow_Up = request.POST.get("Second_Follow_Up")
              Medical_Status = request.POST.get("Medical_Status")
              File_Closure_Status = request.POST.get("File_Closure_Status")
              Remarks = request.POST.get("Remarks")
              Signature = request.POST.get("Signature")
              uploaded_file = request.FILES.get("photo")
              relative_file_path = ""
              if uploaded_file:
                  # Save photo to directory
                  filename = f"{name}.jpg"
                  photos_dir = os.path.join(settings.MEDIA_ROOT, "photos")

                  if not os.path.exists(photos_dir):
                      os.makedirs(photos_dir)

                  save_path = os.path.join(photos_dir, filename)

                  with open(save_path, "wb") as destination:
                      for chunk in uploaded_file.chunks():
                          destination.write(chunk)

                  relative_file_path = os.path.join("photos", filename)

              data = MasterRecords.objects.create(
                  photo_url=relative_file_path,
                  uqid=uqid,
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
              )
              data.save()
              return redirect("master_records_dashboard")

          return render(request, "master_records.html",{"user":user})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#
# @login_required(login_url='/login/')
#
# def master_records_dashboard(request):
#     datas = MasterRecords.objects.all()
#
#
#     return render(request, "dashboard/master_records_dashboard.html", {"data": datas})
from django.http import HttpResponseRedirect
from django.urls import reverse



def master_records_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
        datas = MasterRecords.objects.all()
        return render(request, "dashboard/master_records_dashboard.html", {"data": datas})

