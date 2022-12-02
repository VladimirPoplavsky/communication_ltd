from django import forms
from.models import *

class ContactUsForm(forms.Form):
    # first_name = forms.CharField(max_length=50, label="First Name")
    # last_name = forms.CharField(max_length=50, label="Last Name")
    # phone_number = forms.CharField(max_length=20, label="Phone")
    # email = forms.EmailField(label="Email")

    # 4 previous fields will be added automatically, because only logged-in user can send "Contact Us" request

    subject = forms.CharField(max_length=255, label="Subject")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Your Message")
