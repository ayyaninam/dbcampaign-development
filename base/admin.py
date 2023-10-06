from django.contrib import admin
from .models import *
# Register your models here.

class LeadsAdmin(admin.ModelAdmin):
    list_display = ('phone_number','name','email_address','service_related')
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','email_address_associate','receiver_email')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Lead, LeadsAdmin)
admin.site.register(NewsLetterEmail)
