from django.contrib import admin
from .models import Profile


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone']
    list_filter = ['city']

admin.site.register(Profile, AdminProfile)
