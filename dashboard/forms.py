from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Staff_UserAuth    
from django.contrib.auth.forms import UserCreationForm
     
   


# class AdminUserCreationForm(UserCreationForm):
#     groups = forms.ModelMultipleChoiceField(
#         queryset=Group.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = Staff_UserAuth  # Use your custom user model
#         fields = ('name','email', 'mobile_number','password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             user.groups.set(self.cleaned_data["groups"])
#         return user

# class AdminUserCreationForm(UserCreationForm):
#     groups = forms.ModelMultipleChoiceField(
#         queryset=Group.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = Staff_UserAuth
#         fields = ('name', 'email', 'mobile_number', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             user.groups.set(self.cleaned_data["groups"])
#         return user

class AdminUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Staff_UserAuth
        fields = ('name', 'email', 'mobile_number', 'password1', 'password2')  # Add 'name' field here

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.groups.set(self.cleaned_data["groups"])
        return user




class UserGroupForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['groups']

class UserDeleteForm(forms.Form):
    confirm_deletion = forms.BooleanField(required=True)


