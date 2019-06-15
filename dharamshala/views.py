from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Shala, Booking,vlog
from django.contrib.auth.models import User
from .forms import NewBookingForm,NewVlogForm,Feedback_form
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def search (request):
    query = request.GET.get('q')
    if query:
        queryset = Shala.objects.filter(Q(name_without_space__icontains=query) | Q(name_with_space__icontains=query)
        | Q(city_or_location__icontains=query) | Q(state__icontains=query) | Q(description__icontains=query))
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
    queryset = Shala.objects.all()
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

def shala_vlog_descp(request,slug,year,month,day,hour,minute,second,username):
    shala = get_object_or_404(Shala,name_without_space=slug)
    my_vlog = get_object_or_404(vlog, dharamshala__name_without_space=slug, last_updated__year=year,last_updated__month=month,last_updated__day=day,
    last_updated__hour=hour,last_updated__minute=minute,last_updated__second=second,writer__username=username)
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

@login_required
def booking(request,slug):
    shala = get_object_or_404(Shala,name_without_space=slug)
    if request.method == 'POST':
        form = NewBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.dharamshala = shala
            booking.booked_by = request.user
            booking.save()
            messages.success(request, 'You have requuested for provisional booking at '+str(booking.dharamshala)+'. Our team will shortly contact you. Thank you for using GoJainYatra.')
            return redirect ('user_bookings')
    else:
        form = NewBookingForm()
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
def user_bookings_descp(request,username,year,month,day,hour,minute,second):
    booking = get_object_or_404(Booking,booked_by__username=username,booked_at__year=year,booked_at__month=month,booked_at__day=day,
    booked_at__hour=hour,booked_at__minute=minute,booked_at__second=second)
    return render(request,'user_bookings_descp.html',{'booking':booking})