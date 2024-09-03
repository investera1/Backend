from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .serializers import RegisterUserSerializer

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Specify the fields to display in the admin interface
    list_display = ['username', 'email', 'social_media_links']
    # Specify the fields to be used in the admin form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'social_media_links')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'social_media_links')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
