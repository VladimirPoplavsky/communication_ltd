from django import forms
from .models import ContactUsRequest


class ContactUsForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=50, label="First Name")
    # last_name = forms.CharField(max_length=50, label="Last Name")
    # phone_number = forms.CharField(max_length=20, label="Phone")
    # email = forms.EmailField(label="Email")

    # 4 previous fields will be added automatically, because only logged-in user can send "Contact Us" request
    #
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), label="Your Message")

    class Meta:
        model = ContactUsRequest
        fields = ['subject', 'message']
