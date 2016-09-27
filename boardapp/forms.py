from django import forms

class CreateThread(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    deletion_password = forms.CharField()