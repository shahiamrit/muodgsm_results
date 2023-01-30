from django import forms

class ResultForm(forms.Form):
    symb = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Enter Symbol#'}))
    dob = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Enter Date of Birth#'}))