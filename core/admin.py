from django.contrib import admin

from .models import Email, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")


class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Email, EmailAdmin)
