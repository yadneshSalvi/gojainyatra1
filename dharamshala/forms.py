from django import forms
from .models import Booking,vlog,Feedback
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime


class NewBookingForm(forms.ModelForm):
    checkin_date = forms.DateField(
        widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )
    checkout_date = forms.DateField(
        widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )
    phone_no = forms.CharField(max_length = 10, min_length = 10)

    def clean(self):
        cleaned_data = super(NewBookingForm, self).clean()
        First_Name = cleaned_data['First_Name']
        Last_Name = cleaned_data['Last_Name']
        email_id = cleaned_data['email_id']
        phone_no = cleaned_data['phone_no']
        checkin_date = cleaned_data['checkin_date']
        checkout_date = cleaned_data['checkout_date']
        room_type = cleaned_data['room_type']
        if (datetime.now().date()>checkin_date or datetime.now().date()>checkout_date):
            raise forms.ValidationError("Please enter valid dates")
        return cleaned_data
    class Meta:
        model = Booking
        fields = ['First_Name','Last_Name','email_id','phone_no','checkin_date','checkout_date','room_type','Number_of_adults','Number_of_children']
    
class NewVlogForm(forms.ModelForm):
    blog = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 15, 'placeholder': 'Write about your experience here... eg. cleanliness, customer service, overall review, feedback, etc.'}
        ),
        max_length=5000,
        help_text='The max length of the text is 5000.'
    )

    class Meta:
        model = vlog
        fields = ['blog','image1','image2','image3','image4','image5','image6','image7']

class Feedback_form(forms.ModelForm):
    Feedback = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 15, 'placeholder': 'Suggestions please :)'}
        ),
        max_length=5000,
        help_text='The max length of the text is 5000.'
    )
    class Meta:
        model = Feedback
        fields = ['Feedback','Name']
