from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Shala, Booking,vlog,Voucher
from django.contrib.auth.models import User
from .forms import NewBookingForm,NewVlogForm,Feedback_form,NewVoucherForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import get_messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
from django.utils.formats import localize
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.timezone import localdate
from django.utils.timezone import activate
from test2 import settings
activate(settings.TIME_ZONE)
# Create your views here.

def search (request):
    query = request.GET.get('q')
    if query:
        queryset = Shala.objects.filter(Q(name_without_space__icontains=query) | Q(name_with_space__icontains=query)
        | Q(city_or_location__icontains=query) | Q(state__icontains=query) | Q(description__icontains=query))
        if not queryset:
            messages.error(request, 'Sorry no results found.')
    else:
        queryset = Shala.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 7)

    try:
        shalas = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        shalas = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        shalas = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'shalas':shalas,'query':query})

@method_decorator(login_required, name='dispatch')
class VlogUpdateView(UpdateView):
    model = vlog
    fields = ('blog', 'image1','image2','image3','image4','image5','image6','image7')
    template_name = 'edit_vlog.html'
    pk_url_kwarg = 'vlog_pk'
    context_object_name = 'vlog'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(writer=self.request.user)

    def form_valid(self, form):
        vlog = form.save(commit=False)
        vlog.writer = self.request.user
        vlog.last_updated = timezone.now()
        vlog.save()
        return redirect('shala_vlogs_list', slug=vlog.dharamshala.name_without_space)

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user

def home(request):
    queryset = Shala.objects.all().order_by('ranking')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 9)

    try:
        shalas = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        shalas = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        shalas = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'shalas':shalas})

def shala_info(request,slug):
    shala = get_object_or_404(Shala,name_without_space=slug)
    return render(request,'shala_info.html',{'shala':shala})

def shala_vlog_descp(request,slug,year,month,day,hour,minute,username):
    shala = get_object_or_404(Shala,name_without_space=slug)
    my_vlog = get_object_or_404(vlog, dharamshala__name_without_space=slug, last_updated__year=year,last_updated__month=month,last_updated__day=day,
    last_updated__hour=hour,last_updated__minute=minute,writer__username=username)
    return render(request,'shala_vlog_descp.html',{'shala':shala,'vlog':my_vlog})

def shala_vlogs_list(request,slug):
    shala = get_object_or_404(Shala,name_without_space=slug)
    return render(request,'shala_vlogs_list.html',{'shala':shala})

def contact_us(request):
    if request.method == 'POST':
        form = Feedback_form(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            messages.success(request, 'Thank you for giving us your feedback. We will act on it promptly')
            return redirect (request.path_info)
    else:
        form = Feedback_form()
    return render(request,'contact_us.html',{'form':form})

def vlogs(request):
    shalas = Shala.objects.all()
    return render(request,'vlogs.html',{'shalas':shalas})

def list_dharamshala(request):
    shalas = Shala.objects.all()
    return render(request,'list_dharamshala.html',{'shalas':shalas})


def booking(request,slug):
    shala = get_object_or_404(Shala,name_without_space=slug)
    room_types = []
    if shala.rooms_type1:
        room_types.append(str(shala.rooms_type1))
    if shala.rooms_type2:
        room_types.append(str(shala.rooms_type2))
    if shala.rooms_type3:
        room_types.append(str(shala.rooms_type3))
    if shala.rooms_type4:
        room_types.append(str(shala.rooms_type4))
    if shala.rooms_type5:
        room_types.append(str(shala.rooms_type5))
    if shala.rooms_type6:
        room_types.append(str(shala.rooms_type6))
    if shala.rooms_type7:
        room_types.append(str(shala.rooms_type7))
    if shala.rooms_type8:
        room_types.append(str(shala.rooms_type8))
    if shala.rooms_type9:
        room_types.append(str(shala.rooms_type9))
    if shala.rooms_type10:
        room_types.append(str(shala.rooms_type10))
    if shala.rooms_type11:
        room_types.append(str(shala.rooms_type11))
    if shala.rooms_type12:
        room_types.append(str(shala.rooms_type12))
    if shala.rooms_type13:
        room_types.append(str(shala.rooms_type13))
    if shala.rooms_type14:
        room_types.append(str(shala.rooms_type14))
    if shala.rooms_type15:
        room_types.append(str(shala.rooms_type15))
    if request.method == 'POST':
        form = NewBookingForm(request.POST)
        form.fields['room_type'].choices=[(r,r)for r in room_types]

        if form.is_valid():
            cin = form.cleaned_data.get('checkin_date')
            cout = form.cleaned_data.get('checkout_date')
            if shala.NAfromDate1:
                if ((shala.NAfromDate1 <=cin and cin<= shala.NAtoDate1) or (shala.NAfromDate1 <cout and cout< shala.NAtoDate1) or (cin<=shala.NAfromDate1 and shala.NAfromDate1<cout)):
                    messages.error(request,'Sorry booking for this dharamhala is not available between the dates '+str(localize(shala.NAfromDate1))+' to '+str(localize(shala.NAtoDate1))+'. Please select other dates or search for another Dharamshala')
                    return redirect('booking',slug=shala.name_without_space)
            if shala.NAfromDate2:
                if ((shala.NAfromDate2 <=cin and cin<= shala.NAtoDate2) or (shala.NAfromDate2 <cout and cout< shala.NAtoDate2) or (cin<=shala.NAfromDate2 and shala.NAfromDate2<cout)):
                    messages.error(request,'Sorry booking for this dharamhala is not available between the dates '+str(localize(shala.NAfromDate2))+' to '+str(localize(shala.NAtoDate2))+'. Please select other dates or search for another Dharamshala')
                    return redirect('booking',slug=shala.name_without_space)
            if shala.NAfromDate3:
                if ((shala.NAfromDate3 <=cin and cin<= shala.NAtoDate3) or (shala.NAfromDate3 <cout and cout< shala.NAtoDate3) or (cin<=shala.NAfromDate3 and shala.NAfromDate3<cout)):
                    messages.error(request,'Sorry booking for this dharamhala is not available between the dates '+str(localize(shala.NAfromDate3))+' to '+str(localize(shala.NAtoDate3))+'. Please select other dates or search for another Dharamshala')
                    return redirect('booking',slug=shala.name_without_space)
            if shala.NAfromDate4:
                if ((shala.NAfromDate4 <=cin and cin<= shala.NAtoDate4) or (shala.NAfromDate4 <cout and cout< shala.NAtoDate4) or (cin<=shala.NAfromDate4 and shala.NAfromDate4<cout)):
                    messages.error(request,'Sorry booking for this dharamhala is not available between the dates '+str(localize(shala.NAfromDate4))+' to '+str(localize(shala.NAtoDate4))+'. Please select other dates or search for another Dharamshala')
                    return redirect('booking',slug=shala.name_without_space)
            if shala.NAfromDate5:
                if ((shala.NAfromDate5 <=cin and cin<= shala.NAtoDate5) or (shala.NAfromDate5 <cout and cout< shala.NAtoDate5) or (cin<=shala.NAfromDate5 and shala.NAfromDate5<cout)):
                    messages.error(request,'Sorry booking for this dharamhala is not available between the dates '+str(localize(shala.NAfromDate5))+' to '+str(localize(shala.NAtoDate5))+'. Please select other dates or search for another Dharamshala')
                    return redirect('booking',slug=shala.name_without_space)

            booking = form.save(commit=False)
            booking.dharamshala = shala
            if request.user.is_authenticated:
                booking.booked_by = request.user
            booking.save()
            first_name = form.cleaned_data.get('First_Name')
            last_name = form.cleaned_data.get('Last_Name')
            phone_no = form.cleaned_data.get('phone_no')
            dharamshala = shala
            checkin_date = form.cleaned_data.get('checkin_date')
            checkout_date = form.cleaned_data.get('checkout_date')
            room_type = form.cleaned_data.get('room_type')
            no_adults = form.cleaned_data.get('Number_of_adults')
            no_children = form.cleaned_data.get('Number_of_children')
            subject = '[GoJainYatra]Received Booking request for '+str(dharamshala)+'.'
            #mail_body = 'Hello '+str(first_name)+', we received your request for provisional booking at '+str(booking.dharamshala)+'. Our team will shortly contact you. Thank you for using GoJainYatra.'
            to_email = form.cleaned_data.get('email_id')
            dict_context = {'first_name': first_name,'last_name':last_name,'phone_no':phone_no,'dharamshala':dharamshala,'checkin_date':checkin_date,'checkout_date':checkout_date,'room_type':room_type,'no_adults':no_adults,'no_children':no_children}
            send_mail(subject,get_template('provisional_booking.html').render(dict_context),'GoJainYatra<support@gojainyatra.com>',[to_email,],fail_silently=False)
            subject_dhairya = '[GoJainYatra]Received Booking request for '+str(dharamshala)+' from '+str(first_name)+'.'
            #dhairya_mail = 'Name : '+str(first_name)+' '+str(last_name)+'. Phone no. : '+str(phone_no)+'. Dharamshala : '+str(dharamshala)+'. Checkin date: '+str(checkin_date)+' Checkout date: '+str(checkout_date)+'. Room type : '+str(room_type)
            send_mail(subject_dhairya,
            get_template('dhairya_provisional_booking.html').render(dict_context),'GoJainYatra<support@gojainyatra.com>',['support@gojainyatra.com','rasilabengangar51@gmail.com','starbooking9@gmail.com',],fail_silently=False,
            html_message=get_template('dhairya_provisional_booking.html').render(dict_context),)
            messages.success(request, 'You have requested for provisional booking at '+str(booking.dharamshala)+'. Our team will shortly contact you. Thank you for using GoJainYatra.')
            if not request.user.is_authenticated:
                return redirect('home')
            return redirect ('user_bookings')
        
    else:
        form = NewBookingForm()
        form.fields['room_type'].choices=[(r,r)for r in room_types]
    return render(request,'booking.html',{'shala':shala,'form':form})

@login_required
def write_vlog(request,slug):
    shala = get_object_or_404(Shala,name_without_space=slug)
    if request.method == 'POST':
        form = NewVlogForm(request.POST)
        if form.is_valid():
            vlog = form.save(commit=False)
            vlog.dharamshala = shala
            vlog.writer = request.user
            vlog.save()
            return redirect ('shala_vlogs_list',slug=shala.name_without_space)
    else:
        form = NewVlogForm()
    return render(request,'write_vlog.html',{'shala':shala,'form':form})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(booked_by__username=request.user).order_by('-booked_at')
    return render(request,'user_bookings.html',{'bookings':bookings})

@login_required
def user_vlogs(request):
    vlogs = request.user.vlogs.all()
    return render(request,'user_vlogs.html',{'vlogs':vlogs})

@login_required
def user_bookings_descp(request,username,year,month,day,hour,minute,booking_pk_p):
    booking = get_object_or_404(Booking,booked_by__username=username,booked_at__year=year,booked_at__month=month,booked_at__day=day,
    booked_at__hour=hour,booked_at__minute=minute,pk=booking_pk_p)
    return render(request,'user_bookings_descp.html',{'booking':booking})

@staff_member_required
def pre_voucher(request):
    bookings = Booking.objects.all().order_by('-booked_at')
    return render(request,'pre_voucher.html',{'bookings':bookings})

@staff_member_required
def voucher_form(request,first_name,last_name,year,month,day,hour,minute,booking_pk_p):
    booking = get_object_or_404(Booking,First_Name=first_name,Last_Name=last_name,booked_at__year=year,booked_at__month=month,
    booked_at__day=day,booked_at__hour=hour,booked_at__minute=minute,pk=booking_pk_p)
    request.session['booking_pk']=int(booking.pk)
    if request.method == 'POST':
        form = NewVoucherForm(request.POST)
        if form.is_valid():
            voucher = form.save(commit=False)
            voucher.save()
            pk = voucher.pk
            
            return redirect ('voucher_send',pk=pk)
    else:
        yatri_name = str(booking.First_Name)+' '+str(booking.Last_Name)
        today_date = str(localize(localdate()))
        name_dharamshala = str(booking.dharamshala.name_with_space)
        address = str(booking.dharamshala.description) #this is dharamshala address
        yatri_email = str(booking.email_id)
        yatri_phone = str(booking.phone_no)
        if booking.Number_of_children!=0:
            no_of_yatris = str(booking.Number_of_adults)+' adults, '+str(booking.Number_of_children)+' children'
        else:
            no_of_yatris = str(booking.Number_of_adults)+' adults'
        if booking.room_type!='select' and booking.room_type!=None:
            no_and_type_of_room = str(booking.room_type)
        else:
            no_and_type_of_room = '-'
        checkin_date = str(localize(booking.checkin_date))
        checkout_date = str(localize(booking.checkout_date))
        total_days_of_stay = int((booking.checkout_date-booking.checkin_date).days)
        data_dict = {'yatri_name':yatri_name,'today_date':today_date,'type_of_dharamshala_or_bunglow_or_sanatorium':'Dharamshala',
        'name_of_dharamshala_or_bunglow_or_sanatorium':name_dharamshala,'dharamshala_address':address,'yatri_email':yatri_email,
        'yatri_phone':yatri_phone,'no_of_yatris':no_of_yatris,'no_and_type_of_room':no_and_type_of_room,
        'checkin_date':checkin_date,'checkout_date':checkout_date,'total_days_of_stay':total_days_of_stay}
        form = NewVoucherForm(initial=data_dict)
    return render(request,'voucher_form.html',{'booking':booking,'form':form})

@staff_member_required
def voucher_send(request,pk):
    voucher = get_object_or_404(Voucher,pk=pk)
    return render(request,'voucher_send.html',{'voucher':voucher})

@method_decorator(staff_member_required, name='dispatch')
class VoucherUpdateView(UpdateView):
    model = Voucher
    fields = ('yatri_name','today_date','type_of_dharamshala_or_bunglow_or_sanatorium',
        'name_of_dharamshala_or_bunglow_or_sanatorium','dharamshala_address','phone_of_dharamshala_or_bunglow_or_sanatorium',
        'email_of_dharamshala_or_bunglow_or_sanatorium','check_in_time_given_by_dharamshala',
        'check_out_time_given_by_dharamshala',
        'yatri_email','yatri_phone','yatri_address','no_of_yatris','no_and_type_of_room','checkin_date','checkout_date',
        'check_in_time_given_by_yatri','check_out_time_given_by_yatri',
        'total_days_of_stay','amount_received','service_charge','booking_number','bank_ref_no',
        'gojainyatra_email_id','gojainyatra_phone_no')
    template_name = 'edit_voucher.html'
    pk_url_kwarg = 'voucher_pk'
    context_object_name = 'voucher'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def form_valid(self, form):
        voucher = form.save(commit=False)
        voucher.save()
        return redirect('voucher_send', pk=voucher.pk)

@staff_member_required
def voucher_send_success(request,pk):
    voucher = get_object_or_404(Voucher,pk=pk)
    booking_pk = request.session['booking_pk']
    booking = get_object_or_404(Booking,pk=booking_pk)
    booking.status = int(2)
    booking.save()
    request.session.pop('booking_pk', None)
    request.session.modified = True
    subject = '[GoJainYatra] Confirmation Booking Voucher'
    to_email = voucher.yatri_email
    send_mail(subject,
        get_template('voucher_email.html').render(
            {
                    'voucher':voucher,
                }
            ),
            'GoJainYatra<support@gojainyatra.com>',
            [to_email,]
            ,fail_silently=False,
            html_message=get_template('voucher_email.html').render(
                {
                    'voucher':voucher,
                }
            ),
        )
    return render(request,'voucher_send_success.html',{'voucher':voucher})