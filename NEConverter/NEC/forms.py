from django import forms

class UserInputForms(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'style': 'height: 30px'}))
