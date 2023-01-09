from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Details, uploaded_files

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Details',
            {
                'fields': (
                    'fname',
                    'city',
                    'public_visibility',
                    'birth_date',
                    'age',
                    'location',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Details)
admin.site.register(uploaded_files)
