from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.
STATUS_CHOICES = (
    ('1', 'Waiting for confirmation'),
    ('2', 'Confirmed'),
)

class Shala(models.Model):
    name_without_space = models.CharField(max_length = 30, unique = True)
    name_with_space = models.CharField(max_length = 30, unique = True)
    rooms_starting_at = models.IntegerField()
    description = models.CharField(max_length = 400)
    city_or_location = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    air_conditioner = models.BooleanField(default=False)
    attached_WC = models.BooleanField(default=False)
    attached_Indian_toilet = models.BooleanField(default=False)
    WiFi = models.BooleanField(default=False)
    Driver_Accomodation = models.BooleanField(default=False)
    Generator = models.BooleanField(default=False)
    RO_water = models.BooleanField(default=False)
    Hot_water = models.BooleanField(default=False)
    Locker = models.BooleanField(default=False)
    Parking = models.BooleanField(default=False)
    Lift = models.BooleanField(default=False)
    Bed = models.BooleanField(default=False)
    Water_cooler = models.BooleanField(default=False)
    rooms_type1 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type2 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type3 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type4 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type5 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type6 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type7 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type8 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type9 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type10 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type11 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type12 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type13 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type14 = models.CharField(max_length=400,null=True,blank=True)
    rooms_type15 = models.CharField(max_length=400,null=True,blank=True)
    rule_1 = models.CharField(max_length=400,null=True,blank=True)
    rule_2 = models.CharField(max_length=400,null=True,blank=True)
    rule_3 = models.CharField(max_length=400,null=True,blank=True)
    rule_4 = models.CharField(max_length=400,null=True,blank=True)
    rule_5 = models.CharField(max_length=400,null=True,blank=True)
    rule_6 = models.CharField(max_length=400,null=True,blank=True)
    rule_7 = models.CharField(max_length=400,null=True,blank=True)
    rule_8 = models.CharField(max_length=400,null=True,blank=True)
    rule_9 = models.CharField(max_length=400,null=True,blank=True)
    rule_10 = models.CharField(max_length=400,null=True,blank=True)
    rule_11 = models.CharField(max_length=400,null=True,blank=True)
    rule_12 = models.CharField(max_length=400,null=True,blank=True)
    rule_13 = models.CharField(max_length=400,null=True,blank=True)
    rule_14 = models.CharField(max_length=400,null=True,blank=True)
    rule_15 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_1 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_2 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_3 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_4 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_5 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_6 = models.CharField(max_length=400,null=True,blank=True)
    bhojanshla_rule_7 = models.CharField(max_length=400,null=True,blank=True)
    NAfromDate1 = models.DateField(null=True,blank=True)
    NAtoDate1 = models.DateField(null=True,blank=True)
    NAfromDate2 = models.DateField(null=True,blank=True)
    NAtoDate2 = models.DateField(null=True,blank=True)
    NAfromDate3 = models.DateField(null=True,blank=True)
    NAtoDate3 = models.DateField(null=True,blank=True)
    NAfromDate4 = models.DateField(null=True,blank=True)
    NAtoDate4 = models.DateField(null=True,blank=True)
    NAfromDate5 = models.DateField(null=True,blank=True)
    NAtoDate5 = models.DateField(null=True,blank=True)
    image1 = models.ImageField(upload_to='images/',blank=True,null=True)
    image2 = models.ImageField(upload_to='images/',blank=True,null=True)
    image3 = models.ImageField(upload_to='images/',blank=True,null=True)
    image4 = models.ImageField(upload_to='images/',blank=True,null=True)
    image5 = models.ImageField(upload_to='images/',blank=True,null=True)
    image6 = models.ImageField(upload_to='images/',blank=True,null=True)
    image7 = models.ImageField(upload_to='images/',blank=True,null=True)
    image8 = models.ImageField(upload_to='images/',blank=True,null=True)
    image9 = models.ImageField(upload_to='images/',blank=True,null=True)
    image10 = models.ImageField(upload_to='images/',blank=True,null=True)
    image11 = models.ImageField(upload_to='images/',blank=True,null=True)
    image12 = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.name_with_space
        
    def get_last_vlog(self):
        return vlog.objects.filter(dharamshala=self).order_by('-last_updated').first()

    def get_all_vlogs(self):
        return vlog.objects.filter(dharamshala=self).order_by('-last_updated')

class vlog(models.Model):
    blog = models.TextField(max_length=5000)
    image1 = models.ImageField(upload_to='images/',blank=True,null=True)
    image2 = models.ImageField(upload_to='images/',blank=True,null=True)
    image3 = models.ImageField(upload_to='images/',blank=True,null=True)
    image4 = models.ImageField(upload_to='images/',blank=True,null=True)
    image5 = models.ImageField(upload_to='images/',blank=True,null=True)
    image6 = models.ImageField(upload_to='images/',blank=True,null=True)
    image7 = models.ImageField(upload_to='images/',blank=True,null=True)
    dharamshala = models.ForeignKey(Shala,related_name='vlogs',on_delete=models.CASCADE)
    writer = models.ForeignKey(User,related_name='vlogs',on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_blog = Truncator(self.blog)
        return truncated_blog.chars(15)

    def get_blog_as_markdown(self):
        return mark_safe(markdown(self.blog, safe_mode='escape'))

class Booking(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=10)
    checkin_date = models.DateField(default=timezone.now)
    checkout_date = models.DateField(default=timezone.now)
    room_type = models.CharField(max_length=100,blank=True,null=True,default="select")
    dharamshala = models.ForeignKey(Shala,related_name='bookings',on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User,related_name='bookings',on_delete=models.CASCADE,null=True,blank=True)
    booked_at = models.DateTimeField(default=timezone.now)
    Number_of_adults = models.IntegerField(null=True, blank=True, default=1)
    Number_of_children = models.IntegerField(null=True, blank=True, default=0)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='1')
    #in final model change above field to auto_now_add = True
    def __str__(self):
        return self.First_Name

    #def clean(self):
    #    if (self.dharamshala.NAfromDate1<=self.checkin_date and self.checkin_date<=self.dharamshala.NAtoDate1):
    #       raise ValidationError('Sorry booking of this dharamshala is not available between the dates '+str(self.dharamshala.NAfromDate1)+' to '+str(self.dharamshala.NAtoDate1))
    #def get_all_bookings(self):
    #    return bookings.objects.order_by('-last_updated')

class Feedback(models.Model):
    Feedback = models.TextField(max_length=5000)
    Name = models.CharField(max_length=50)

    def __str__(self):
        name ='user_feedback'
        if self.Name:
            return self.Name
        return name

class Voucher(models.Model):
    yatri_name = models.CharField(max_length=100)
    today_date = models.CharField(max_length=100,blank=True,null=True)
    type_of_dharamshala_or_bunglow_or_sanatorium = models.CharField(max_length=100)
    name_of_dharamshala_or_bunglow_or_sanatorium = models.CharField(max_length=100)
    address = models.TextField(max_length=500,blank=True,null=True)
    phone_of_dharamshala_or_bunglow_or_sanatorium = models.CharField(max_length=12,blank=True,null=True)
    yatri_email = models.EmailField(blank=True,null=True)
    yatri_phone = models.CharField(max_length=12)
    no_of_yatris = models.CharField(max_length=100,blank=True,null=True)
    no_and_type_of_room = models.CharField(max_length=100,blank=True,null=True)
    checkin_date = models.CharField(max_length=100,blank=True,null=True)
    checkout_date = models.CharField(max_length=100,blank=True,null=True)
    total_days_of_stay = models.CharField(max_length=3,blank=True,null=True)
    amount_received = models.CharField(max_length=100,blank=True,null=True)
    booking_number = models.CharField(max_length=100,blank=True,null=True)
    bank_ref_no = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.yatri_name