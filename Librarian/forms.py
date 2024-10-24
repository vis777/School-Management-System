from django import forms

class LibrarianLoginForm(forms.Form):  # Updated form class name
    librarian_user_name = forms.CharField(max_length=100)  # Updated field name
    librarian_pass_word = forms.CharField(widget=forms.PasswordInput)  # Updated field name
