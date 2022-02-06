from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """User Profile Admin"""
    list_display = (
        'user',
        'street_address1',
        'street_address2',
        'postcode',
        'city',
    )


admin.site.register(UserProfile)
