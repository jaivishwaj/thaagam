from collections import UserDict
from datetime import timezone
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from django.contrib.auth import authenticate, login


# from .models import CustomUser
import os
from django.conf import settings

from django.urls import reverse


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Provision

from django.contrib.auth import logout

# from .models import userprofile
from .models import UserProfile

# from formapp.models import Staff_UserAuth


from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
import datetime
# from formapp.models import Staff_UserAuth, userprofile
from django.contrib.auth import get_user_model
User = get_user_model()
from formapp.forms import userprofileForm


from .models import *

@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
# def signupuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         mobile_number = request.POST.get('mobile_number')
#         confrimpassword = request.POST.get('confrimpassword')
#         gcc_name = request.POST.get('gcc_name')
#         gcc_location = request.POST.get('gcc_location')
#
#         User = get_user_model()  # Get the custom user model
#         if not User.objects.filter(username=username).exists():
#             # Create a new user instance and set the username
#             user = User.objects.create_user(username= username,  password=password)
#             Userprofile=userprofile.objects.create(username=username, email=email, password=password, mobile_number=mobile_number,confrimpassword=confrimpassword,gcc_name=gcc_name, gcc_location=gcc_location)
#             # Save the user
#             Userprofile.save()
#             user.save()
#             return redirect('login')  # Redirect to login upon successful registration
#         else:
#             # Authentication failed, handle accordingly (e.g., display an error message)
#             messages.info(request, f'The Username Exit plz sign in with new username or try with different spelling')
#             return redirect('signup')
#
#     return render(request, 'signup.html')

# def signupuser(request):
#     if request.method == 'POST':
#         form = userprofileForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             confirm_password = form.cleaned_data['confirm_password']
#             gcc_name = form.cleaned_data['gcc_name']
#             gcc_location = form.cleaned_data['gcc_location']
#             role = form.cleaned_data['role']
#
#             # Create user
#             user = UserProfile.objects.create_user(username=username, email=email, password=password,confirm_password=confirm_password, gcc_name=gcc_name,
#                                                    gcc_location=gcc_location, role=role)
#
#             # Assign user to group based on role
#             if role == 'superuser':
#                 group = Group.objects.get(name='superuser')
#             else:
#                 group = Group.objects.get(name='staff')
#             user.groups.add(group)
#
#             return redirect('login')  # Redirect to login page after successful signup
#     else:
#         form = userprofileForm()
#     return render(request, 'signup.html', {'form': form})

######### private view start ########

def signupuser(request):
    if request.method == 'POST':
        form = __userprofileForm(request.POST)  # Using a hypothetical private form class
        if form.is_valid():
            username = form.cleaned_data['__username']
            email = form.cleaned_data['__email']
            password = form.cleaned_data['__password']
            confirm_password = form.cleaned_data['__confirm_password']
            gcc_name = form.cleaned_data['__gcc_name']
            gcc_location = form.cleaned_data['__gcc_location']
            role = form.cleaned_data['__role']

            # Create user
            user = UserProfile.objects.create_user(username=username, email=email, password=password,
                                                   confirm_password=confirm_password, gcc_name=gcc_name,
                                                   gcc_location=gcc_location, role=role)

            # Assign user to group based on role
            if role == 'superuser':
                group = Group.objects.get(name='superuser')
            else:
                group = Group.objects.get(name='staff')
            user.groups.add(group)

            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = __userprofileForm()  # Using a hypothetical private form class
    return render(request, 'signup.html', {'form': form})


######### private view end ########



@csrf_exempt
def loginuser(request):
    if request.method == 'POST':
        # gcc_name = request.POST.get('gcc_name')
        username = request.POST.get('username')  # Assuming 'username' is the field name
        password = request.POST.get('password')


        # Check if the user is an admin
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # User is an admin and authentication successful, log the user in
            login(request, user)
            # You can perform additional actions after login if needed
            request.session['user'] = user.username  # Storing username in session
            return redirect('home')  # Redirect to a success page (replace 'home' with your URL name)

        else:
            # Authentication failed or user is not an admin, handle accordingly (e.g., display an error message)
            messages.error(request, 'Invalid username or password for admin login.')

    return render(request, 'registration/login.html')


# def loginuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         gcc_name = request.POST.get('gcc_name')
#         gcc_location = request.POST.get('gcc_location')
#
#         # Check if the user exists based on username and additional fields
#         user = authenticate(request, username=username, password=password, gcc_name=gcc_name, gcc_location=gcc_location)
#
#         if user is not None:
#             # Check if the user is a superuser or staff member
#             if user.is_superuser or user.is_staff:
#                 login(request, user)
#
#                 # Add user to the 'staff' group if not already a member
#                 staff_group, created = Group.objects.get_or_create(name='staff')
#                 if not user.groups.filter(name='staff').exists():
#                     staff_group.user_set.add(user)
#
#                 messages.success(request, 'Logged in successfully.')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'You do not have permission to access this site.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#
#     return render(request, 'registration/login.html')


def logout_view(request):
    request.session.flush()
    return redirect("login")



def home(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    return render(request, "home.html",{'user': user})


from django.contrib.auth import authenticate,login
@csrf_exempt
def accident_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    
    if request.method == "POST":
        print("post",request.POST)
        uqid = request.POST.get("uqid")
        date = request.POST.get("date")
        inmate_name = request.POST.get("inmate_name")
        age_gender = request.POST.get("age_gender")
        accident_condition = request.POST.get("accident_condition")
        accident_place = request.POST.get("accident_place")
        signature = request.POST.get("signature")
        logged_in_user = request.user
        username = logged_in_user.username
        
        data = AccidentRegister.objects.create(
            user=username,
            uqid=uqid,
            date=date,
            inmate_name=inmate_name,
            age_gender=age_gender,
            accident_condition=accident_condition,
            accident_place=accident_place,
            signature=signature,
            
        )
        data.save()
        
        
        return redirect("accident_register_dashboard")
    else:
        messages.info(request, 'The form is not saved. Please re-enter the form')
        accidents = AccidentRegister.objects.all().order_by('-created_at') 
    
    return render(request, "accident_register.html", {'user': user,'data': accidents})

                                                                                             

# from django.shortcuts import objects
@csrf_exempt
 
def accident_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
       return redirect("login")
    else: 
      logged_in_username = request.user.username
      datas = AccidentRegister.objects.filter(user=logged_in_username)
      return render( request, "dashboard/accident_register_dashboard.html", {"data": datas})
    
@csrf_exempt

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
        uploaded_file = request.FILES.get("photo")
        relative_file_path = ""
        if uploaded_file:
            # Save photo to directory
            filename = f"{resident_name}.jpg"
            photos_dir = os.path.join(settings.MEDIA_ROOT, "photos")

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            relative_file_path = os.path.join("photos", filename)
        
        logged_in_user = request.user
        username = logged_in_user.username

        data = Reintegration.objects.create(user=username,
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
            photo_url=relative_file_path,
            
        )
        data.save()

        return redirect("reintegration_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        reintegration = Reintegration.objects.all().order_by('-created_at')
    return render(request, "reintegration_register.html",{'user': user, 'reintegration': reintegration})




def reintegration_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
        logged_in_username = request.user.username
        datas = Reintegration.objects.filter(user=logged_in_username)
        return render(request, "dashboard/reintegration_register_dashboard.html", {"data": datas})
    

@csrf_exempt

def visitor_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']

    if request.method == "POST":
        date = request.POST.get("date")
        name = request.POST.get("name")
       
        whom_to_see = request.POST.get("whom_to_see")
        in_time = request.POST.get("in_time")
        out_time = request.POST.get("out_time")
        phone_number = request.POST.get("phone_number")
        signature = request.POST.get("signature")
        logged_in_user = request.user
        username = logged_in_user.username
        data = VisitorRegister.objects.create(user=username,
            date=date,
           
            name=name,
            whom_to_see=whom_to_see,
            in_time=in_time,
            out_time=out_time,
            phone_number=phone_number,
            signature=signature
        )
        data.save()
        return redirect("visitor_registration_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        datas = VisitorRegister.objects.all().order_by('-created_at')
    return render(request, "visitor_registration.html",{'user': user, 'data': datas})


def visitor_registration_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = VisitorRegister.objects.filter(user=logged_in_username)
     return render(
        request, "dashboard/visitor_registration_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = PerformanceAppraisal.objects.create(user=username,
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
            rescue=rescue


        )
        data.save()
        return redirect("performance_appraisal_dashboard")  # Redirect to appropriate page after form submission
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        Performance = PerformanceAppraisal.objects.all().order_by('-created_at')

    return render(request, "performance_appraisal.html",{'user': user, 'Performance': Performance})



def performance_appraisal_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = PerformanceAppraisal.objects.filter(user=logged_in_username)
     return render(
        request, "dashboard/performance_appraisal_dashboard.html", {"data": datas})


@csrf_exempt

def provision_form(request):
    user= None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == 'POST':

        material_name = request.POST['material_name']
        total_quantity = request.POST['total_quantity']
        utilized_quantity = request.POST['utilized_quantity']
        balance_quantity = request.POST['balance_quantity']
        remarks = request.POST['remarks']
        logged_in_user = request.user
        username = logged_in_user.username
        data=Provision.objects.create(user=username,
            material_name=material_name,
            total_quantity=total_quantity,
            utilized_quantity=utilized_quantity,
            balance_quantity=balance_quantity,
            remarks=remarks
        )
        data.save()
        return redirect('provision_dashboard')
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        provision = Provision.objects.all().order_by('-created_at')

    return render(request, 'provision.html',{'user': user,'provision': provision})


def provision_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")

    else:

     logged_in_username = request.user.username
     datas = Provision.objects.filter(user=logged_in_username)

     return render(
        request, "dashboard/provision_dashboard.html", {"data": datas})

@csrf_exempt

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
        daysabsent = request.POST.get("daysabsent")
        logged_in_user = request.user
        username = logged_in_user.username

        data = Resident.objects.create(user=username,
            pupilName=pupilName,
            dob=dob,uqid=uqid,
            attendance=attendance,
            daysPresent=daysPresent,
            daysAbsent=daysabsent
        )

        data.save()

        return redirect("resident_attendance_form_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        resident = Resident.objects.all().order_by('-created_at')
    return render(request, "resident_attendance.html",{'user': user,'resident': resident})


def resident_attendance_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Resident.objects.filter(user=logged_in_username)
     return render(
        request, "dashboard/resident_attendance_form_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        # Create a new instance of your model
        data = SocialEntertainment.objects.create(user=username,
            date=date,uqid=uqid, admission=admission, name=name, workDetails=workDetails
        )

        data.save()

        return redirect("social_entertainment_form_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        social = SocialEntertainment.objects.all().order_by('-created_at')

    return render(request, "social_entertainment_record.html",{'user': user,'social': social})


def social_entertainment_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = SocialEntertainment.objects.filter(user=logged_in_username)
     return render(
        request, "dashboard/social_entertainment_form_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        # Create an instance of the model and save data
        data = Inspectionregister.objects.create(user=username,
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
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        inspection = Inspectionregister.objects.all().order_by('-created_at')

    return render(request, "inspection_register.html",{'user': user,'inspection': inspection})



def inspection_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Inspectionregister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/inspection_records_dashboard.html", {"data": datas})


@csrf_exempt

def case_history_form(request):
    print("case history form",request.POST)
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        religion = request.POST.get("religion")
        maritalStatus = request.POST.get("maritalStatus")
        identificationMark = request.POST.get("identificationMark")
        educationBackground = request.POST.get("educationBackground")
        occupation = request.POST.get("occupation")
        address = request.POST.get("address")
        residentContactNumber = request.POST.get("residentContactNumber")
        relativeOrFriendsContact = request.POST.get("relativeOrFriendsContact")
        idProofAvailable = request.POST.get("idProofAvailable")
        idProofDetails = request.POST.get("idProofDetails")
        policeMemoAvailable = request.POST.get("policeMemoAvailable")
        policeStationDetails = request.POST.get("policeStationDetails")
        
        logged_in_user = request.user
        username = logged_in_user.username
        uploaded_file = request.FILES.get("photo")

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


            data = CaseHistory.objects.create(photo_url = relative_file_path,
                                                uqid=uqid,
                                                user=username,
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
                                                policeStationDetails=policeStationDetails)
            data.save()
            
            return redirect('case_history_record_dashboard')
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        case = CaseHistory.objects.all().order_by('-created_at')

    return render(request,'case_history.html',{'user': user,'case': case})



def case_history_record_dashboard(request):
    if not request.user.is_authenticated:
       return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = CaseHistory.objects.filter(user=logged_in_username)
     return render(request, "dashboard/case_history_record_dashboard.html",{"data": datas})
 
 
@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

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
            data = PersonalInfo.objects.create(user=username,
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
        else:
            messages.info(request, f'the form is not saved please re enter the form')
    else:
        personalinfo = PersonalInfo.objects.all().order_by('-created_at')
    personalinfo = personalinfo[::-1]
    return render(request, "personal_information.html",{'user': user,'personalinfo': personalinfo})



def personal_info_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = PersonalInfo.objects.filter(user=logged_in_username)
     return render(
        request, "dashboard/personal_information_dashboard.html",{"data": datas})
     
     
@csrf_exempt

def actionplan_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date_of_plan = request.POST.get("date_of_plan")
        detailed_notes = request.POST.get("detailed_notes")
        action_plan_date = request.POST.get("action_plan_date")
        logged_in_user = request.user
        username = logged_in_user.username

        data = ActionplanRegister.objects.create(user=username,
            date_of_plan=date_of_plan,
            detailed_notes=detailed_notes,
            action_plan_date=action_plan_date,
        )

        data.save()

        return redirect("action_plan_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        action = ActionplanRegister.objects.all().order_by('-created_at')

    return render(request, "actionplan_register.html",{'user': user,'action': action})



def action_plan_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = ActionplanRegister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/action_plan_dashboard.html",{"data": datas})

@csrf_exempt

def awarnes_register_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        date = request.POST.get("date")
        time = request.POST.get("time")
        place = request.POST.get("place")
        details = request.POST.get("details")
        participants = request.POST.get("participants")
        logged_in_user = request.user
        username = logged_in_user.username
        data = AwarnesRegister.objects.create(user=username,
            uqid=uqid,
            date=date,
            time=time,
            place=place,
            details=details,
            participants=participants,
        )

        data.save()

        return redirect("awarnes_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        awarnes = AwarnesRegister.objects.all().order_by('-created_at')

    return render(request, "awarnes_register.html",{'user': user,'awarnes': awarnes})


def awarnes_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = AwarnesRegister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/awarnes_register_dashboard.html",{"data": datas})


@csrf_exempt
def asset_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        # uqid = request.POST.get("uqid")
        date_purchase = request.POST.get("date_purchase")
        name_asset = request.POST.get("name_asset")
        no_of_items = request.POST.get("no_of_items")
        cost = request.POST.get("cost")
        bill_no = request.POST.get("bill_no")
        place_asset = request.POST.get("place_asset")
        owner_asset = request.POST.get("owner_asset")
        dispose_date = request.POST.get("dispose_date")
        what_dispossed = request.POST.get("what_dispossed")
        logged_in_user = request.user
        username = logged_in_user.username
        data = Asset.objects.create(user=username,
            # uqid=uqid,
            date_purchase=date_purchase,
            name_asset=name_asset,
            no_of_items=no_of_items,
            cost=cost,
            bill_no=bill_no,
            place_asset=place_asset,
            owner_asset=owner_asset,
            dispose_date=dispose_date,
            what_dispossed=what_dispossed,
        )

        data.save()

        return redirect("asset_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        asset = Asset.objects.all().order_by('-created_at')

    return render(request, "asset.html",{'user': user,'asset': asset})
def asset_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Asset.objects.filter(user=logged_in_username)
     return render(request, "dashboard/asset_register_dashboard.html",{"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = BpPulsenote.objects.create(user=username,
            date=date, uqid=uqid, name=name, pulse=pulse, bp=bp, temperature=temperature
        )


        data.save()

        return redirect("bp_form_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        bp = BpPulsenote.objects.all().order_by('-created_at')

    return render(request, "bp_pulsenote.html",{'user': user,'bp': bp})


def bp_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = BpPulsenote.objects.filter(user=logged_in_username)
     return render(request, "dashboard/bp_form_dashboard.html",{"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username


        data = CounsellingRegister.objects.create(user=username,
            date=date,
            uqid=uqid,
            name=name,
            number_of_sessions=number_of_sessions,
            observation_identification=observation_identification,
            signature=signature,
        )

        data.save()

        return redirect("counselling_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        counselling = CounsellingRegister.objects.all().order_by('-created_at')

    return render(request, "counselling_register.html",{'user': user,'counselling': counselling})


def counselling_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = CounsellingRegister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/counselling_register_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = MedicalCamp.objects.create(user=username,
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
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        medical = MedicalCamp.objects.all().order_by('-created_at')

    return render(request, "medical_camp.html",{'user': user,'medical': medical})


def medical_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = MedicalCamp.objects.filter(user=logged_in_username)
     return render(request, "dashboard/medical_register_dashboard.html",{"data": datas})


@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        datas = Medicine.objects.create(uqid=uqid,user=username,
            name=name,
            age=age,
            type_of_disease=type_of_disease,
            tablet_details=tablet_details,
        )

        datas.save()

        return redirect("medicine_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        medicine = Medicine.objects.all().order_by('-created_at')

    return render(request, "medicine.html",{'user': user,'medicine': medicine})


def medicine_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Medicine.objects.filter(user=logged_in_username)
     return render(request, "dashboard/medicine_register_dashboard.html",{"data": datas})

@csrf_exempt

def night_survey_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
       
        time = request.POST.get("time")
        place = request.POST.get("place")
        details_of_visit = request.POST.get("details_of_visit")
        number_of_rescue = request.POST.get("number_of_rescue")
        logged_in_user = request.user
        username = logged_in_user.username
        data = NightSurvey.objects.create(user=username,
            date=date,
    
            time=time,
            place=place,
            details_of_visit=details_of_visit,
            number_of_rescue=number_of_rescue,
        )
        data.save()
        return redirect("night_survey_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        night = NightSurvey.objects.all().order_by('-created_at')

    return render(request, "night_survey.html",{'user': user,'night': night})



def night_survey_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = NightSurvey.objects.filter(user=logged_in_username)
     return render(request, "dashboard/night_survey_dashboard.html",{"data": datas})

@csrf_exempt

def skill_training_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        uqid = request.POST.get("uqid")
        date = request.POST.get("date")
        resident_name = request.POST.get("resident_name")
        skill_training_details = request.POST.get("skill_training_details")
        logged_in_user = request.user
        username = logged_in_user.username
        datas = SkillTraining.objects.create(user=username,
            uqid=uqid,
            date=date,
            resident_name=resident_name,
            skill_training_details=skill_training_details,
        )
        datas.save()
        return redirect("skill_training_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        skill = SkillTraining.objects.all().order_by('-created_at')

    return render(request, "skill_training.html",{'user': user,'skill': skill})


def skill_training_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = SkillTraining.objects.filter(user=logged_in_username)
     return render(request, "dashboard/skill_training_dashboard.html",{"data": datas})

@csrf_exempt

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
        gcc_officials_name = request.POST.get("gcc_officials_name")
        ngo_staff_name = request.POST.get("ngo_staff_name")   
        police_officials_name = request.POST.get("police_officials_name")
        residents_name = request.POST.get("residents_name")
        logged_in_user = request.user
        username = logged_in_user.username
        datas = SmcRegister.objects.create(user=username,
            date=date,
            time=time,
            introduction_of_meeting=introduction_of_meeting,
            last_month_performance_details=last_month_performance_details,
            issue_resolved=issue_resolved,
            this_month_issue=this_month_issue,
            gcc_officials_name=gcc_officials_name,
            ngo_staff_name=ngo_staff_name,           
            police_officials_name=police_officials_name,
            residents_name=residents_name,
        )
        datas.save()
        return redirect("smc_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        smc = SmcRegister.objects.all().order_by('-created_at')

    return render(request, "smc_register.html",{'user': user,'smc': smc})


def smc_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = SmcRegister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/smc_register_dashboard.html",{"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username
        datas = StaffAttendance.objects.create(user=username,
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
        messages.info(request, f'the form is not saved please re enter the form')
        staffatt = StaffAttendance.objects.all().order_by('-created_at')
    return render(request, "staff_attendance.html",{'user': user,'staffatt': staffatt})


def staff_attendance_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
      logged_in_username = request.user.username
      datas = StaffAttendance.objects.filter(user=logged_in_username)
      return render(
          request, "dashboard/staff_attendance_register_dashboard.html", {"data": datas})

@csrf_exempt

def stock_form(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
    if request.method == "POST":
        date = request.POST.get("date")
        
        particulars = request.POST.get("particulars")
        receipt = request.POST.get("receipt")
        issued = request.POST.get("issued")
        balance = request.POST.get("balance")
        logged_in_user = request.user
        username = logged_in_user.username
        datas = Stock.objects.create(user=username,
            date=date,
            
            particulars=particulars,
            receipt=receipt,
            issued=issued,
            balance=balance,
        )
        datas.save()
        return redirect("stock_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        stock = Stock.objects.all().order_by('-created_at')

    return render(request, "stock_register.html",{'user': user,'stock': stock})


def stock_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Stock.objects.filter(user=logged_in_username)
     return render(request, "dashboard/stock_register_dashboard.html",{"data": datas})

@csrf_exempt

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
        
        logged_in_user = request.user
        username = logged_in_user.username
        
        datas = EmploymentLink.objects.create(user=username,
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
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        employmenyt = EmploymentLink.objects.all().order_by('-created_at')

    return render(request, "employment_link.html",{'user': user,'employmenyt': employmenyt})


def employment_linkage_form_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
      logged_in_username = request.user.username
      datas = EmploymentLink.objects.filter(user=logged_in_username)
      return render( request, "dashboard/employment_linkage_form_dashboard.html",{"data": datas})


from django.utils import timezone
@csrf_exempt

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
        uploaded_file = request.FILES.get("photo")
        print('uploaded_file_photo',uploaded_file)
        print('request.post',request.POST)
        relative_file_path = ""
        if uploaded_file:
            # Save photo to directory
            filename = f"{name_of_the_resident}.jpg"
            photos_dir = os.path.join(settings.MEDIA_ROOT, "photos")

            if not os.path.exists(photos_dir):
                os.makedirs(photos_dir)

            save_path = os.path.join(photos_dir, filename)

            with open(save_path, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            relative_file_path = os.path.join("photos", filename)

        
        logged_in_user = request.user
        username = logged_in_user.username
        
        datas = Rehabitation.objects.create(user=username,
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
            photo_url=relative_file_path,
        )
        datas.save()
        
        return redirect("rehabitation_dashboard")
    else:
        messages.info(request, 'The form is not saved. Please re-enter the form.')
        
    # Get all data, ordered by created_at
    rehab = Rehabitation.objects.all().order_by('-created_at')
    
    # Get data created today
    today_rehab = Rehabitation.objects.filter(created_at__date=timezone.now().date())
    
    return render(request, "rehabitation.html", {'user': user, 'rehab': rehab, 'today_rehab': today_rehab})

def rehabitation_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = Rehabitation.objects.filter(user=logged_in_username)
     return render(request, "dashboard/rehabitation_dashboard.html",{"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = DeathRegister.objects.create(user=username,
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
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        death = DeathRegister.objects.all().order_by('-created_at')
    return render(request, "death_register.html",{'user': user,'death': death})


def death_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = DeathRegister.objects.filter(user=logged_in_username)
     return render(request, "dashboard/death_register_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = FoodMenu(user=username,
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
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        food = FoodMenu.objects.all().order_by('-created_at')
    return render(request, "food_menu.html",{'user': user,'food': food})


def food_menu_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
       logged_in_username = request.user.username
       datas = FoodMenu.objects.filter(user=logged_in_username)
       return render(request, "dashboard/food_menu_dashboard.html", {"data": datas})

@csrf_exempt

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
        logged_in_user = request.user
        username = logged_in_user.username

        data = SalaryRegister(user=username,date=date,uqid=uqid, name=name, designation=designation, salary=salary, sign=sign)

        data.save()
        return redirect("salary_register_dashboard")
    else:
        messages.info(request, f'the form is not saved please re enter the form')
        salary = SalaryRegister.objects.all().order_by('-created_at')
    return render(request, "salary_register.html",{'user': user,'salary': salary})


def salary_register_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
       logged_in_username = request.user.username
       datas = SalaryRegister.objects.filter(user=logged_in_username)
       return render(request, "dashboard/salary_register_dashboard.html",{"data": datas})

@csrf_exempt

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
              logged_in_user = request.user
              username = logged_in_user.username

              data = StaffMovement(user=username,
                  date_of_plan=date_of_plan,
                  uqid=uqid,
                  working_area=working_area,
                  nature_of_work=nature_of_work,
                  work_done_by=work_done_by,
                  sign=sign,
              )
              data.save()

              return redirect("staff_movement_note_dashboard")
        else:
            messages.info(request, f'the form is not saved please re enter the form')
            staffmov = StaffMovement.objects.all().order_by('-created_at')

        return render(request, "staff_movement_note.html",{'user': user,'staffmov': staffmov})

# @login_required(login_url='/login/')

def staff_movement_note_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
     logged_in_username = request.user.username
     datas = StaffMovement.objects.filter(user=logged_in_username)
     return render(request, "dashboard/staff_movement_note_dashboard.html",{"data": datas})


@csrf_exempt

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
        Family_Contact_No = request.POST.get("Family_Contact_No")
        Relation = request.POST.get("Relation")
        Permanent_Address = request.POST.get("Permanent_Address")
        Mode_Of_Identification_Rescue = request.POST.get("Mode_Of_Identification_Rescue")
        Identification_Mark = request.POST.get("Identification_Mark")
        Identification_Papers = request.POST.get("Identification_Papers")
        Rehabilitation_Measures = request.POST.get("Rehabilitation_Measures")
        Reason_For_Leaving_Shelter = request.POST.get("Reason_For_Leaving_Shelter")
        Action_takenup = request.POST.get("Action_takenup")
        Follow_Up_Action = request.POST.get("Follow_Up_Action")
        Medical_Status = request.POST.get("Medical_Status")
        File_Closure_Status = request.POST.get("File_Closure_Status")
        police_memo = request.POST.get("police_memo")
        police_Station = request.POST.get("police_Station")
        Fact_finding = request.POST.get("Fact_finding")
        Signature = request.POST.get("Signature")
        uploaded_file = request.FILES.get("photo")
        logged_in_user = request.user
        username = logged_in_user.username
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

        logged_in_user = request.user
        username = logged_in_user.username

        data = MasterRecords.objects.create(user=username,
            photo_url=relative_file_path,
            uqid=uqid,
            name=name,
            Aid_no=Aid_no,
            Age_gender=Age_gender,
            dob=dob,
            Date_Of_Admission=Date_Of_Admission,
            Family_Contact_No=Family_Contact_No,
            Relation=Relation,
            Permanent_Address=Permanent_Address,
            Mode_Of_Identification_Rescue=Mode_Of_Identification_Rescue,
            Identification_Mark=Identification_Mark,
            Identification_Papers=Identification_Papers,
            Rehabilitation_Measures=Rehabilitation_Measures,
            Reason_For_Leaving_Shelter=Reason_For_Leaving_Shelter,
            Action_takenup=Action_takenup,
            Follow_Up_Action=Follow_Up_Action,
            Medical_Status=Medical_Status,
            File_Closure_Status=File_Closure_Status,
            police_memo=police_memo,
            police_Station=police_Station,
            Fact_finding=Fact_finding,
            Signature=Signature,
        )
        data.save()
        

        # MasterRecords.objects.all().delete()

        return redirect("master_records_dashboard")
    else:
        messages.info(request, 'The form is not saved. Please re-enter the form')
        master = MasterRecords.objects.all().order_by('created_at')

    return render(request, "master_records.html", {"user": user, "master": master})



                                                       
def master_records_dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page with a message
        return redirect("login")
    else:
        logged_in_username = request.user.username
        datas = MasterRecords.objects.filter(user=logged_in_username)
        return render(request, "dashboard/master_records_dashboard.html", {"data": datas})



import openpyxl


def download_master_records_excel(request):
    # Fetch all master records from the database
    master_records = MasterRecords.objects.all()

    # Create a new Excel workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Add headers to the worksheet
    ws.append([
        'ID', 'Name', 'Aid No', 'Age/Gender', 'Date of Birth', 'Date of Admission',
        'Date of Leaving', 'Family Contact No', 'Relation', 'Permanent Address',
        'Mode of Identification/Rescue', 'Identification Mark', 'Identification Papers',
        'Rehabilitation Measures', 'Reason for Leaving Shelter', 'Follow Up Action',
        'Second Follow Up', 'Medical Status', 'File Closure Status', 'Police Memo',
        'Police Station', 'Remarks', 'Signature'
    ])

    # Add data from master_records to the worksheet
    for record in master_records:
        ws.append([
            record.id, record.name, record.Aid_no, record.Age_gender, record.dob,
            record.Date_Of_Admission, record.Date_Of_Leaving, record.Family_Contact_No,
            record.Relation, record.Permanent_Address, record.Mode_Of_Identification_Rescue,
            record.Identification_Mark, record.Identification_Papers, record.Rehabilitation_Measures,
            record.Reason_For_Leaving_Shelter, record.Follow_Up_Action,
            record.Medical_Status, record.File_Closure_Status, record.police_memo, record.police_Station,
            record.Fact_finding, record.Signature
        ])

    # Save the workbook to a BytesIO object
    excel_data = openpyxl.writer.excel.save_virtual_workbook(wb)

    # Create an HTTP response with Excel MIME type
    response = HttpResponse(content=excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=master_records.xlsx'

    return response

@csrf_exempt
# 
# def search_results(request):
#     accidentform = None
#     casehistory = None
#     reintegrationform = None
#     salaryform = None
#     medicineform = None
#     medicalform = None
#     counsellingform = None
#     bpform = None
#     awarnesform = None
#     socialentform = None
#     resident = None
#     perfomance = None
#     staffmovement = None
#     staffatt = None
#     personalinfo = None
#     emplink = None
#     rehab = None
#     death = None
#     skill = None
    
#     if 'uqid' in request.GET:
#         uqid = request.GET['uqid']
#         # Fetch all records matching the uqid
#         accidentform = AccidentRegister.objects.filter(uqid__icontains=uqid)
#         casehistory = CaseHistory.objects.filter(uqid__icontains=uqid)
#         reintegrationform = Reintegration.objects.filter(uqid__icontains=uqid)
#         salaryform = SalaryRegister .objects.filter(uqid__icontains=uqid)
#         medicineform = Medicine.objects.filter(uqid__icontains=uqid)
#         medicalform = MedicalCamp.objects.filter(uqid__icontains=uqid)
#         counsellingform = CounsellingRegister.objects.filter(uqid__icontains=uqid)
#         bpform = BpPulsenote.objects.filter(uqid__icontains=uqid)
#         awarnesform = AwarnesRegister.objects.filter(uqid__icontains=uqid)
#         socialentform = SocialEntertainment.objects.filter(uqid__icontains=uqid)
#         resident = Resident.objects.filter(uqid__icontains=uqid)
#         perfomance = PerformanceAppraisal.objects.filter(uqid__icontains=uqid)
#         staffmovement = StaffMovement.objects.filter(uqid__icontains=uqid)
#         staffatt = StaffAttendance.objects.filter(uqid__icontains=uqid)
#         personalinfo = PersonalInfo.objects.filter(uqid__icontains=uqid)
#         emplink = EmploymentLink.objects.filter(uqid__icontains=uqid)
#         rehab = Rehabitation.objects.filter(uqid__icontains=uqid)
#         death = DeathRegister.objects.filter(uqid__icontains=uqid)
#         skill = SkillTraining.objects.filter(uqid__icontains=uqid)
        
#         print('accidentform,',accidentform)
    
#     return render(request, 'dashboard/records.html', {'accident': accidentform, 'casehistory': casehistory, 'reintegration': reintegrationform,
#                                                       'salaryform': salaryform,'medicineform':medicineform,'medicalform':medicalform,
#                                                       'counsellingform':counsellingform,'bpform':bpform,'awarnesform':awarnesform,
#                                                       'socialentform':socialentform,'resident':resident,'perfomance':perfomance,
#                                                       'staffmovement':staffmovement,'staffatt':staffatt,'personalinfo':personalinfo,
#                                                       'emplink':emplink,'rehab':rehab,'death':death,'skill':skill})
@login_required
# @permission_required('formapp.can_view_dashboard', raise_exception=True)
  
def search_results(request):
    query_param = request.GET.get('uqid', '')
    records = {}

    models_to_search = [
        AccidentRegister, CaseHistory, Reintegration, SalaryRegister,
        Medicine, MedicalCamp, CounsellingRegister, BpPulsenote,
        AwarnesRegister, SocialEntertainment, Resident, PerformanceAppraisal,
        StaffMovement, StaffAttendance, PersonalInfo, EmploymentLink,
        Rehabitation, DeathRegister, SkillTraining
    ]

    for model in models_to_search:
        records[model.__name__.lower()] = model.objects.filter(uqid__icontains=query_param)

    return render(request, 'dashboard/records.html', {'records': records})    

    
@csrf_exempt

def case_work(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']

    if request.method == 'POST':
        print("in post",request.POST)
        uqid = request.POST.get('uqid')
        photo = request.FILES.get('photo')
        aid_no = request.POST.get('aid_no')
        doa = request.POST.get('doa')
        dol = request.POST.get('dol')
        mode_of_rescue = request.POST.get('mode_of_rescue')
        file_details = request.POST.get('file_details')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        marital_status = request.POST.get('marital_status')
        idnt_mark = request.POST.get('idnt_mark')
        edu_back = request.POST.get('edu_back')
        occcu_back = request.POST.get('occcu_back')
        address = request.POST.get('address')
        resident_ph = request.POST.get('resident_ph')
        relative_ph = request.POST.get('relative_ph')
        id_proof = request.POST.get('id_proof')
        police_memo = request.POST.get('police_memo')
        res_photo1 = request.FILES.get('res_photo1')
        res_photo2 = request.FILES.get('res_photo2')
        res_letter = request.POST.get('res_letter')
        small_narration = request.POST.get('small_narration')
        geno1 = request.FILES.get('geno1')
        geno2 = request.FILES.get('geno2')
        genogram = request.POST.get('genogram')
        res_family = request.POST.get('res_family')
        res_eco = request.POST.get('res_eco')
        res_phy_status = request.POST.get('res_phy_status')
        hl_photo1 = request.FILES.get('hl_photo1')
        hl_photo2 = request.FILES.get('hl_photo2')
        reason_for_homeless = request.POST.get('reason_for_homeless')
        stre_and_weak = request.POST.get('stre_and_weak')
        fact = request.POST.get('fact')
        rehab_photo1 = request.FILES.get('rehab_photo1')
        rehab_photo2 = request.FILES.get('rehab_photo2')
        rehab_measure = request.POST.get('rehab_measure')
        action = request.POST.get('action')
        followup1 = request.POST.get('followup1')
        followup2 = request.POST.get('followup2')
        followup3 = request.POST.get('followup3')
        
        
        logged_in_user = request.user
        username = logged_in_user.username
        
        
        data = CaseWork.objects.create(user=username,
                                       uqid=uqid,
                                       photo=photo,
                                       aid_no=aid_no,
                                       doa=doa,
                                       dol=dol,
                                       mode_of_rescue=mode_of_rescue,
                                       file_details=file_details,
                                       name=name,
                                       age=age,
                                       gender=gender,
                                       religion=religion,
                                       marital_status=marital_status,
                                       idnt_mark=idnt_mark,
                                       edu_back=edu_back,
                                       occcu_back=occcu_back,
                                       address=address,
                                       resident_ph=resident_ph,
                                       relative_ph=relative_ph,
                                       id_proof=id_proof,
                                       police_memo=police_memo,
                                       res_photo1=res_photo1,
                                       res_photo2=res_photo2,
                                       res_letter=res_letter,
                                       small_narration=small_narration,
                                       geno1=geno1,
                                       geno2=geno2,
                                       genogram=genogram,
                                       res_family=res_family,
                                       res_eco=res_eco,
                                       res_phy_status=res_phy_status,
                                       hl_photo1=hl_photo1,
                                       hl_photo2=hl_photo2,
                                       reason_for_homeless=reason_for_homeless,
                                       stre_and_weak=stre_and_weak,
                                       fact=fact,
                                       rehab_photo1=rehab_photo1,
                                       rehab_photo2=rehab_photo2,
                                       rehab_measure=rehab_measure,
                                       action=action,
                                       followup1=followup1,
                                       followup2=followup2,
                                       followup3=followup3
                                       )
        
        data.save()
         
        
        return redirect('case_work_dashboard')
    else:
        messages.success(request, 'Case work data saved successfully.')
        case_work = CaseWork.objects.all().order_by('created_at')

    return render(request,'case_work.html',{'user':user,'case_work':case_work})


# def case_work(request):
#     user = request.session.get('user')
#     case_work = CaseWork.objects.all().order_by('created_at')

#     if request.method == 'POST':
#         form = CaseWork(request.POST, request.FILES)
#         if form.is_valid():
#             case_work_instance = form.save(commit=False)
#             case_work_instance.user = request.user.username
#             case_work_instance.save()
#             messages.success(request, 'Case work data saved successfully.')
#             return redirect('case_work_dashboard')
#         else:
#             messages.error(request, 'Failed to save case work data. Please check the form.')
#     else:
#         form = CaseWork()

#     return render(request, 'case_work.html', {'user': user, 'form': form, 'case_work': case_work})


def case_work_dashboard(request): 
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logged_in_username = request.user.username
        datas = CaseWork.objects.filter(user=logged_in_username)
        return render(request, "dashboard/case_work_dashboard.html", {"data": datas})
@csrf_exempt
@login_required
def follow_up(request):
    user = None
    if 'user' in request.session:
        user = request.session['user']
        
    if request.method == 'POST':
        uqid = request.POST.get('uqid')
        name = request.POST.get('name')
        date = request.POST.get('date')
        follow_up = request.POST.get('follow_up')
        
        logged_in_user = request.user
        username = logged_in_user.username
        
        data = FollowUP.objects.create(user=username,
                                       uqid=uqid,
                                       name=name,
                                       date=date,
                                       follow_up=follow_up
                                       )
        data.save()
        return redirect('followup_dashboard')
    else:
        messages.success(request, 'Follow up data saved successfully.')
        follow_up = FollowUP.objects.all().order_by('created_at')
        
    return render(request,'followup.html',{'user':user,'follow_up':follow_up})
      


def followup_dashboard(request): 
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logged_in_username = request.user.username
        datas = FollowUP.objects.filter(user=logged_in_username)
        return render(request, "dashboard/followup_dashboard.html", {"data": datas})
    


from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group



