from django import forms

class sForm(forms.Form):
    sform = scode_no = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Data Entry Asst. Name'}))