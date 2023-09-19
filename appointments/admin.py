from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appid', 'fullname', 'email', 'phone', 'datebooking', 'serviceid', 'docid', 'note', 'timebooking')
    list_filter = ('fullname',)
    search_fields = ('fullname',)

admin.site.register(Appointment, AppointmentAdmin)