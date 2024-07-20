from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .functions import superuser, staff




def superuser_or_administrator(user):
    return user.is_superuser or user.groups.filter(name='Administrator').exists()

# Example view that requires superuser or administrator permissions
@user_passes_test(superuser_or_administrator)
def protected_view(request):
    return HttpResponse("You have superuser or administrator permissions.")



@login_required
@user_passes_test(lambda u: u.is_superuser)
def superuser_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            staff_members = User.objects.filter(is_staff=True)
            return render(request, 'superuser_dashboard.html', {'staff_members': staff_members})
        # else:
        #     return redirect('login1')  # Redirect to login if user is not a superuser
        else:
            return redirect('superuser_dashboard')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def staff_dashboard(request, staff_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            staff = User.objects.get(id=staff_id)
            return render(request, 'staff_dashboard.html', {'staff': staff})
        # else:
        #     return redirect('login1')  # Redirect to login if user is not a superuser
        else:
            return redirect('staff_dashboard')


@login_required
@user_passes_test(superuser_or_administrator)
def register(request):
    if request.method == "POST":
        form = AdminUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "User successfully registered.")

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




def user_login(request):
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

    return render(request, "login.html")


GROUPS = ["superuser", "staff"]


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_control_panel(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = get_object_or_404(User, pk=user_id)

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

    users = User.objects.all()
    return render(
        request,
        "dashboard/user_control_panel.html",
        {
            "users": users,
            "groups": GROUPS,
        },
    )
