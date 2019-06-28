"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from dharamshala import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('vlogs/',views.vlogs,name='vlogs'),
    path('signup/',accounts_views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dharamshala/search/',views.search,name='search'),
    path('reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    path('user_bookings/',views.user_bookings,name='user_bookings'),
    path('user_bookings/<username>/<year>/<month>/<day>/<hour>/<minute>/<booking_pk_p>',views.user_bookings_descp,name='user_bookings_descp'),
    path('user_vlogs/',views.user_vlogs,name='user_vlogs'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dharamshala/<slug:slug>/',views.shala_info,name='shala_info'),
    path('dharamshala/<slug:slug>/vlogs/',views.shala_vlogs_list,name='shala_vlogs_list'),
    path('dharamshala/<slug:slug>/vlogs/<year>/<month>/<day>/<hour>/<minute>/<username>/',views.shala_vlog_descp,name='shala_vlog_descp'),
    path('dharamshala/<slug:slug>/vlogs/<year>/<month>/<day>/<hour>/<minute>/<username>/<vlog_pk>/edit/',views.VlogUpdateView.as_view(),name='edit_vlog'),
    path('list_dharamshala/',views.list_dharamshala,name='list_dharamshala'),
    path('dharamshala/<slug:slug>/booking/',views.booking,name='booking'),
    path('dharamshala/<slug:slug>/write_vlog/',views.write_vlog,name='write_vlog'),
    path('after_booking/confirmation/generate/pre_voucher',views.pre_voucher,name='pre_voucher'),
    path('gen/<first_name>/<last_name>/<year>/<month>/<day>/<hour>/<minute>/<booking_pk_p>/form/',views.voucher_form,name='voucher_form'),
    path('gen/<pk>/send/',views.voucher_send,name='voucher_send'),
    path('gen/<voucher_pk>/edit/',views.VoucherUpdateView.as_view(),name='edit_voucher'),
    path('gen/<pk>/sent/',views.voucher_send_success,name='voucher_send_success')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
