from django import forms

class ResultForm(forms.Form):
    symb = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Symbol No.'}))
    dob = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'DOB: YYYY-MM-DD'}))