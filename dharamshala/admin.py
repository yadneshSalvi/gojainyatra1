from django.contrib import admin
from .models import Shala,vlog,Booking,Feedback
from easy_maps.widgets import AddressWithMapWidget
from django import forms

# Register your models here.

class ShalaAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address_for_google_map': AddressWithMapWidget({'class': 'vTextField'})
            }
    ordering = ('ranking',)

admin.site.register(Shala,ShalaAdmin)
admin.site.register(vlog)
admin.site.register(Booking)
admin.site.register(Feedback)