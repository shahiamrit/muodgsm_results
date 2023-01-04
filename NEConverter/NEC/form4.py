from django import forms

class ResultForm(forms.Form):
    scode_no = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Enter Secret Code#'}))