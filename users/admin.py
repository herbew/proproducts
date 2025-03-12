from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User

class UserAdmin(AuthUserAdmin):
    # Determines which fields to display on the user list page.
    list_display = ('username', 'email', 'name', 'type', 'gender', 'is_staff')
    
    # Defines the fields that can be used for searching.
    search_fields = ('username', 'email', 'name')
    
    # Determine the filters available in the sidebar
    list_filter = ('type', 'gender', 'is_staff', 'is_superuser')
    
    # Define field grouping on the user details page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email', 'type', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Defines which fields can be filled in when adding a new user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'name', 'email', 'type', 'gender'),
        }),
    )

# Registering the User model to the Django admin
admin.site.register(User, UserAdmin)