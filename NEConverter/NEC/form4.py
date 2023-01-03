from django import forms

class ResultForm(forms.Form):
    phone_no = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Enter Phone#'}))