from django.contrib import admin

from .models import Email, Phone, Profile, Services


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "brand", "position")


class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("profile", "number", "label", "is_primary")


class ServicesAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "description")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Services, ServicesAdmin)
