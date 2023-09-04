from django.contrib import admin
from .models import AuthUserGroups

# Register your models here.
class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group')
    list_filter = ()
    search_fields = ()


admin.site.register(AuthUserGroups, AuthUserGroupsAdmin)