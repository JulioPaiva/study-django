from django.contrib import admin

from .models import Email, Phone, Posts, Profile, Services, Skills


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "brand", "position")


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("profile", "number", "label", "is_primary")


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "description")


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
