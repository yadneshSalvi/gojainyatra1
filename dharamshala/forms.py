from django import forms
from .models import Booking,vlog,Feedback,Voucher
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime


class NewBookingForm(forms.ModelForm):
    checkin_date = forms.DateField(
    widget=forms.TextInput(
        attrs={'type': 'date',
                'class':'datepicker',
                'data-target': '#datepicker1',
            } 
        ),
    initial=datetime.now().date()
    )         
    checkout_date = forms.DateField(
    widget=forms.TextInput(
        attrs={'type': 'date',
                'class':'datepicker',
                'data-target': '#datepicker1',
            } 
        ),
    initial=datetime.now().date()
    )
    phone_no = forms.CharField(max_length = 10, min_length = 10)

    def clean(self):
        cleaned_data = super(NewBookingForm, self).clean()
        if not ('checkin_date' in cleaned_data.keys() and 'checkout_date' in cleaned_data.keys()):
            raise forms.ValidationError("Please enter valid dates")
        else:
            checkin_date = cleaned_data['checkin_date']
            checkout_date = cleaned_data['checkout_date']
        if (datetime.now().date()>checkin_date or datetime.now().date()>checkout_date):
            raise forms.ValidationError("Please enter valid dates")
        if (checkin_date>checkout_date):
            raise forms.ValidationError("Check out date should be after Checkin date")
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

class NewVoucherForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3}
        ),
        max_length=500,
    )
    class Meta:
        model = Voucher
        fields = ['yatri_name','today_date','type_of_dharamshala_or_bunglow_or_sanatorium',
        'name_of_dharamshala_or_bunglow_or_sanatorium','address','phone_of_dharamshala_or_bunglow_or_sanatorium',
        'yatri_email','yatri_phone','no_of_yatris','no_and_type_of_room','checkin_date','checkout_date',
        'total_days_of_stay','amount_received','booking_number','bank_ref_no']
