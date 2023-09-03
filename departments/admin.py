from django.contrib import admin
from .models import Departments

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('departmentid', 'named', 'get_doctors_count')
    list_filter = ('named',)
    search_fields = ('named',)

    def get_doctors_count(self, obj):
        return obj.doctors_count

    get_doctors_count.short_description = 'Doctors Count'

admin.site.register(Departments, DepartmentsAdmin)
