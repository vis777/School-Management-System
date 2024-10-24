from django import forms

class AdminLoginForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Username")
    pass_word = forms.CharField(widget=forms.PasswordInput, label="Password")
