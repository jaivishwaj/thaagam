from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from dashboard.forms import AdminUserCreationForm
from dashboard.functions import is_administrator, superuser_or_administrator
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render


from dashboard.models import Staff_UserAuth

@login_required
# @permission_required('formapp.dashboard', raise_exception=True)


def list_users(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'dashboard/dashboard.html', {'users': users})


from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Staff_UserAuth


GROUPS = [
    "Administrator",
    "Superuser",
]



@login_required
@user_passes_test(is_administrator)
def user_control_panel(request):
    if request.method == "POST":
        user = request.POST.get("user")
        user = get_object_or_404(User)

        if "change_password" in request.POST:
            new_password = request.POST.get("change_password")
            form_data = {
                "new_password1": new_password,
                "new_password2": new_password,
            }
            password_form = SetPasswordForm(user, form_data)

            if password_form.is_valid():
                password_form.save()
                messages.success(
                    request, f"Password changed successfully for {user.username}."
                )
            else:
                messages.error(request, f"Error changing password for {user.username}.")

        elif (
            "delete_user" in request.POST
            and request.POST.get("confirm_deletion") == "on"
        ):
            user.delete()
            messages.success(request, f"User {user.username} deleted successfully.")

        elif "update_groups" in request.POST:
            new_groups = request.POST.getlist("update_groups")
            user.groups.set([])  # Clear existing groups
            for group_name in new_groups:
                if group_name in GROUPS:
                    group, created = Group.objects.get_or_create(
                        name=group_name.strip()
                    )
                    user.groups.add(group)
                else:
                    messages.error(request, f"Invalid group name: {group_name}")

            messages.success(
                request, f"Groups updated successfully for {user.username}."
            )

        return redirect("user_control_panel")

    users = Staff_UserAuth.objects.all()
    return render(
        request,
        "dashboard/user_control_panel.html",
        {
            "users": users,
            "groups": GROUPS,
        },
    )



@login_required
@user_passes_test(superuser_or_administrator)
def register(request):
    if request.method == "POST":
        form = AdminUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "User successfully registered.")
            if request.POST.get("groups") == "3":
                # Create a new Staff_UserAuth instance
                data = Staff_UserAuth(
                    name=user.name,
                    password=user.password,
                    email=user.email,
                    mobile_number=user.mobile_number,
                    
                )
                # Save the Staff_UserAuth instance
                data.save()
                print(data)
            print("request.POST :", request.POST)
            if request.POST.get("groups") == "3":
                print(3)
            return redirect("dash_reg")

        else:
            for field in form:
                if field.errors:
                    existing_classes = field.field.widget.attrs.get("class", "")
                    field.field.widget.attrs["class"] = f"{existing_classes} is-invalid"
            messages.error(request, "Error registering user.")
    else:
        form = AdminUserCreationForm()

    return render(request, "dashboard/register_user.html", {"form": form})



def dashboard_login(request):
    # Capture the 'next' parameter on initial GET request and save to session
    if request.method == "GET" and "next" in request.GET:
        request.session["next"] = request.GET["next"]

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Retrieve 'next' parameter from session if it exists
            next_url = request.session.pop(
                "next", None
            )  # Use pop to remove it after retrieving
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                # Default redirect if 'next' parameter isn't present
                return redirect(
                    "dashboard"
                )  # Change "dashboard" to your default post-login redirect URL
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "dashboard/login.html")




# def dash_reg(request):
# #     Your view logic here
#      return render(request, "dashboard/register_user.html")

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def dash_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('dashboard_home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register_user.html', {'form': form})