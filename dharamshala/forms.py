from django import forms
from .models import Booking,vlog,Feedback
from django.contrib.admin.widgets import AdminDateWidget


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
    class Meta:
        model = Booking
        fields = ['First_Name','Last_Name','email_id','phone_no','checkin_date','checkout_date','room_type']
    
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
            attrs={'rows': 15, 'placeholder': 'Suggestiongs please :)'}
        ),
        max_length=5000,
        help_text='The max length of the text is 5000.'
    )
    class Meta:
        model = Feedback
        fields = ['Feedback','Name']