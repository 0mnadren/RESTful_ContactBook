from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    # To display in the admin as columns
    list_display = ('id', 'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    # I want to search by email and username
    search_fields = ('email', 'username')
    # This fields can't be changed
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

