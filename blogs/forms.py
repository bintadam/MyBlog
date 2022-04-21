from django import forms
from django.forms import ModelForm
from blogs.models import post
from accounts.models import User
from tinymce.widgets import TinyMCE

class Contactform(forms.Form):
    countries = [("IN","INDIA"),("USA","AMERICA")]
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$",required=False)
    massage = forms.CharField(max_length=500)
    country = forms.ChoiceField(choices=countries) 

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        if email == '' and phone == '':
            raise forms.ValidationError("Atleast email or phone number should be provided" ,code= "invalid")