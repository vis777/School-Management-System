from django import forms

class OfficeStaffLoginForm(forms.Form):
    officestaff_user_name = forms.CharField(max_length=100)
    officestaff_pass_word = forms.CharField(widget=forms.PasswordInput)