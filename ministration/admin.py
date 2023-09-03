from django.contrib import admin
from .models import Ministration

# Register your models here.
class MinistrationAdmin(admin.ModelAdmin):
    list_display = ('minisid','name_ministration','get_appointment_count')
    list_filter = ('name_ministration',)
    search_fields = ('name_ministration',)

    def get_appointment_count(self, obj):
        return obj.appointment_count

    get_appointment_count.short_description = 'Appointment Count'

admin.site.register(Ministration, MinistrationAdmin)
